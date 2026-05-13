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
	Result   interface{} `json:"result,omitempty"`
	Error    interface{} `json:"error,omitempty"`
	ID       int         `json:"id"`
}

var state *core.StateDB

func rpcHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	if r.Method == "OPTIONS" {
		w.WriteHeader(http.StatusOK)
		return
	}

	var req RPCRequest
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	resp := RPCResponse{
		JSONRPC: "2.0",
		ID:      req.ID,
	}

	switch req.Method {
	case "eth_chainId":
		resp.Result = "0x309"

	case "web3_clientVersion":
		resp.Result = "STG-Chain/v0.3"

	case "eth_blockNumber":
		resp.Result = fmt.Sprintf("0x%x", state.GetBlock())

	case "eth_getBalance":
		if len(req.Params) < 1 {
			resp.Error = "missing address param"
			break
		}
		addr := req.Params[0].(string)
		balance := state.GetBalance(addr)
		resp.Result = fmt.Sprintf("0x%x", balance)

	case "eth_sendTransaction":
		if len(req.Params) < 1 {
			resp.Error = "missing transaction parameters"
			break
		}
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
		}

	case "stg_transactions":
		resp.Result = state.GetTransactions()

	default:
		resp.Error = "method not supported"
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}

func StartRPCServer(port int, s *core.StateDB) {
	state = s
	addr := fmt.Sprintf(":%d", port)
	http.HandleFunc("/", rpcHandler)
	fmt.Println("STG RPC listening on", addr)
	err := http.ListenAndServe(addr, nil)
	if err != nil {
		log.Fatal(err)
	}
}
