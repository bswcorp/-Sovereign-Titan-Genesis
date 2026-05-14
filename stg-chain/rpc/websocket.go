package rpc

import (
	"bufio"
	"crypto/sha1"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"net/http"
	"stg-chain/core"
)

type WSResponse struct {
	JSONRPC string      `json:"jsonrpc"`
	Method  string      `json:"method"`
	Params  interface{} `json:"params"`
}

// StartWSServer boots the stateful push engine for the Council of Five
func StartWSServer(port int, state *core.StateDB) {
	http.HandleFunc("/ws", func(w http.ResponseWriter, r *http.Request) {
		if r.Header.Get("Upgrade") != "websocket" {
			http.Error(w, "Protokol upgrade wajib menggunakan WebSocket", http.StatusBadRequest)
			return
		}

		// 🔐 Handshake Challenge Security Protocol
		hj, ok := w.(http.Hijacker)
		if !ok {
			http.Error(w, "Webserver lacks hijacking capabilities", http.StatusInternalServerError)
			return
		}
		conn, bufrw, err := hj.Hijack()
		if err != nil {
			return
		}
		defer conn.Close()

		// Compute cryptographic acceptance key
		key := r.Header.Get("Sec-WebSocket-Key")
		hash := sha1.New()
		hash.Write([]byte(key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"))
		acceptKey := base64.StdEncoding.EncodeToString(hash.Sum(nil))

		// Transmit raw HTTP upgrade response matrix
		bufrw.WriteString("HTTP/1.1 101 Switching Protocols\r\n")
		bufrw.WriteString("Upgrade: websocket\r\n")
		bufrw.WriteString("Connection: Upgrade\r\n")
		bufrw.WriteString(fmt.Sprintf("Sec-WebSocket-Accept: %s\r\n\r\n", acceptKey))
		bufrw.Flush()

		log.Printf("📡 WS CONNECT: Guardian pipeline established with core server node.")

		// Active Event Listener Loop: Intercept data from the StateDB Event Bus channel
		for tx := range state.EventBus {
			payload := WSResponse{
				JSONRPC: "2.0",
				Method:  "stg_subscription",
				Params:  tx,
			}
			jsonBytes, _ := json.Marshal(payload)
			
			// Write unfragmented text frame headers manually (0x81 indicates Text Frame)
			length := len(jsonBytes)
			if length < 126 {
				bufrw.WriteByte(0x81)
				bufrw.WriteByte(byte(length))
				bufrw.Write(jsonBytes)
				bufrw.Flush()
			}
		}
	})

	addr := fmt.Sprintf(":%d", port)
	log.Printf("🔌 WebSocket Event Server streaming active on port %s/ws\n", addr)
}
