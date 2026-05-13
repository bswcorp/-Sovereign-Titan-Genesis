package rpc

import (
	"encoding/json"
	"fmt"
	"net/http"
)

// JSONRPCRequest represents standard Ethereum/STG RPC schema
type JSONRPCRequest struct {
	JsonRPC string        `json:"jsonrpc"`
	Method  string        `json:"method"`
	Params  []interface{} `json:"params"`
	ID      int           `json:"id"`
}

// JSONRPCResponse format for communication
type JSONRPCResponse struct {
	JsonRPC string      `json:"jsonrpc"`
	Result  interface{} `json:"result"`
	Error   interface{} `json:"error,omitempty"`
	ID      int         `json:"id"`
}

// StartRPCServer boots the JSON-RPC interface endpoint
func StartRPCServer(port int) {
	http.HandleFunc("/", handleRPC)
	go func() {
		fmt.Printf("📡 STG-CHAIN RPC LAYER: Active on port :%d\n", port)
		if err := http.ListenAndServe(fmt.Sprintf(":%d", port), nil); err != nil {
			fmt.Printf("🚨 RPC Network Halted: %v\n", err)
		}
	}()
}

func handleRPC(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*") // Izinkan Explorer connect

	if r.Method != "POST" {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var req JSONRPCRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "Bad request", http.StatusBadRequest)
		return
	}

	var result interface{}

	// Route methods directly compatible with the Minimal Explorer backend
	switch req.Method {
	case "eth_blockNumber":
		result = "0x309" // Block number simulation in hex (777)
	case "eth_getBalance":
		result = "0x52b7d2dcc80cd2e4000000" // Simulated balance for Unit 008 wallet
	case "stg_getQuorumStatus":
		result = map[string]interface{}{"quorum": true, "active_validators": 3, "status": "STABLE"}
	default:
		result = "Method not implemented"
	}

	response := JSONRPCResponse{
		JsonRPC: "2.0",
		Result:  result,
		ID:      req.ID,
	}

	json.NewEncoder(w).Encode(response)
}
