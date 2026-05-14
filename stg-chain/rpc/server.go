package rpc

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"
	"stg-chain/core"
)

type RPCRequest struct {
	JSONRPC string        `json:"jsonrpc"`
	Method  string        `json:"method"`
	Params  []interface{} `json:"params"`
	ID      int           `json:"id"`
}

type RPCResponse struct {
	JSONRPC string      `json:"jsonrpc"`
	ID      int         `json:"id"`
	Result  interface{} `json:"result,omitempty"`
	Error   interface{} `json:"error,omitempty"`
}

var stateStore *core.StateDB

func SetStateStore(store *core.StateDB) {
	stateStore = store
}

func handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	if r.Method == "OPTIONS" {
		w.WriteHeader(http.StatusOK)
		return
	}

	var req RPCRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	var result interface{}

	switch req.Method {
	case "eth_blockNumber":
		result = "0x" + strconv.FormatUint(stateStore.GetLatestBlock(), 16)
	case "eth_getBalance":
		if len(req.Params) > 0 {
			addr, _ := req.Params[0].(string)
			result = "0x" + strconv.FormatUint(stateStore.GetBalance(addr), 16)
		} else {
			result = "0x0"
		}
	case "eth_chainId":
		result = "0x309"
	case "net_version":
		result = "777"
	case "web3_clientVersion":
		result = "STG-Chain/v0.1-Quantum"
	default:
		result = null
	}

	resp := RPCResponse{JSONRPC: "2.0", ID: req.ID, Result: result}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}

func StartRPCServer(port int) {
	http.HandleFunc("/", handler)
	addr := fmt.Sprintf(":%d", port)
	log.Printf("STG RPC listening on %s\n", addr)
	if err := http.ListenAndServe(addr, nil); err != nil {
		log.Fatal(err)
	}
}
