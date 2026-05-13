package rpc

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"

	"stg-chain/core"
)

type JSONRPCRequest struct {
	JSONRPC string        `json:"jsonrpc"`
	Method  string        `json:"method"`
	Params  []interface{} `json:"params"`
	ID      int           `json:"id"`
}

type JSONRPCResponse struct {
	JSONRPC string      `json:"jsonrpc"`
	Result  interface{} `json:"result,omitempty"`
	Error   interface{} `json:"error,omitempty"`
	ID      int         `json:"id"`
}

func StartRPCServer(port int, state *core.StateDB) {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {

		body, err := ioutil.ReadAll(r.Body)
		if err != nil {
			http.Error(w, "invalid request body", http.StatusBadRequest)
			return
		}

		var req JSONRPCRequest
		err = json.Unmarshal(body, &req)
		if err != nil {
			http.Error(w, "invalid json", http.StatusBadRequest)
			return
		}

		resp := JSONRPCResponse{
			JSONRPC: "2.0",
			ID:      req.ID,
		}

		switch req.Method {

		case "eth_blockNumber":
			resp.Result = "0x" + strconv.FormatUint(state.GetLatestBlock(), 16)

		case "eth_getBalance":
			if len(req.Params) < 1 {
				resp.Error = "missing address param"
				break
			}

			address, ok := req.Params[0].(string)
			if !ok {
				resp.Error = "invalid address format"
				break
			}

			balance := state.GetBalance(address)
			resp.Result = "0x" + strconv.FormatUint(balance, 16)

		case "web3_clientVersion":
			resp.Result = "STG-Chain/v0.1.0"

		case "net_version":
			resp.Result = "777"

		default:
			resp.Error = "method not supported"
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(resp)
	})

	addr := fmt.Sprintf(":%d", port)

	fmt.Println("RPC server listening on", addr)

	err := http.ListenAndServe(addr, nil)
	if err != nil {
		panic(err)
	}
}
