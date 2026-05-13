package rpc

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"
	"sync"

	"stg-chain/core"
	"github.com"
)

type RPCRequest struct {
	JSONRPC string        `json:"jsonrpc"`
	Method  string        `json:"method"`
	Params  []interface{} `json:"params"`
	ID      int           `json:"id"`
}

type RPCResponse struct {
	JSONRPC string      `json:"jsonrpc"`
	Result  interface{} `json:"result,omitempty"`
	Error   interface{} `json:"error,omitempty"`
	ID      int         `json:"id"`
}

var (
	state     *core.StateDB
	upgrader  = websocket.Upgrader{CheckOrigin: func(r *http.Request) bool { return true }}
	clients   = make(map[*websocket.Conn]bool)
	clientsMu sync.Mutex
)

// BroadcastEvent transmits structured messages to all connected live Web3 dashboards
func BroadcastEvent(event interface{}) {
	clientsMu.Lock()
	defer clientsMu.Unlock()
	data, _ := json.Marshal(event)
	for client := range clients {
		err := client.WriteMessage(websocket.TextMessage, data)
		if err != nil {
			client.Close()
			delete(clients, client)
		}
	}
}

func wsHandler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		return
	}
	clientsMu.Lock()
	clients[conn] = true
	clientsMu.Unlock()
}

func rpcHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	if r.Method == "OPTIONS" {
		w.WriteHeader(http.StatusOK)
		return
	}

	var req RPCRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	resp := RPCResponse{JSONRPC: "2.0", ID: req.ID}

	switch req.Method {
	case "eth_chainId":
		resp.Result = "0x309"
	case "web3_clientVersion":
		resp.Result = "STG-Chain/v0.3-LevelDB"
	case "eth_blockNumber":
		resp.Result = fmt.Sprintf("0x%x", state.GetBlock())
	case "eth_getBalance":
		addr := req.Params[0].(string)
		resp.Result = fmt.Sprintf("0x%x", state.GetBalance(addr))
	case "eth_sendTransaction":
		tx := req.Params[0].(map[string]interface{})
		from := tx["from"].(string)
		to := tx["to"].(string)
		valueStr := tx["value"].(string)
		value, _ := strconv.ParseUint(valueStr, 10, 64)

		hash, err := state.SendTransaction(from, to, value)
		if err != nil {
			resp.Error = err.Error()
		} else {
			resp.Result = hash
			// Push transaction event through WebSocket pipe immediately
			BroadcastEvent(map[string]interface{}{"event": "new_tx", "hash": hash, "from": from, "to": to, "value": value})
		}
	default:
		resp.Error = "method not supported"
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}

func StartRPCServer(rpcPort int, wsPort int, s *core.StateDB) {
	state = s

	// HTTP JSON-RPC Listener
	go func() {
		mux := http.NewServeMux()
		mux.HandleFunc("/", rpcHandler)
		fmt.Printf("HTTP RPC listening on :%d\n", rpcPort)
		_ = http.ListenAndServe(fmt.Sprintf(":%d", rpcPort), mux)
	}()

	// WebSocket Stream Listener
	go func() {
		mux := http.NewServeMux()
		mux.HandleFunc("/events", wsHandler)
		fmt.Printf("WebSocket Stream listening on :%d/events\n", wsPort)
		_ = http.ListenAndServe(fmt.Sprintf(":%d", wsPort), mux)
	}()
}
