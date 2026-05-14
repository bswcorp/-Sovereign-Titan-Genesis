package main

import (
	"flag"
	"fmt"
	"os"
	"time"
	"stg-chain/core"
	"stg-chain/rpc"
)

func main() {
	genesisPath := flag.String("genesis", "core/genesis.json", "Path to genesis configuration")
	rpcPort := flag.Int("rpc.port", 8545, "RPC listening port")
	wsPort := flag.Int("ws.port", 8546, "WebSocket event streaming port")
	flag.Parse()

	fmt.Println("======================================")
	fmt.Println("STG Sovereign Node Booting - M5 Engine Framework")
	fmt.Println("======================================")

	if _, err := os.Stat(*genesisPath); err != nil {
		fmt.Printf("Genesis file not found: %v\n", err)
		os.Exit(1)
	}

	stateStore := core.NewStateDB()
	rpc.SetStateStore(stateStore)

	// ⏳ Auto-Increment Block Height Engine
	go func() {
		for {
			time.Sleep(3 * time.Second)
			stateStore.IncrementBlock()
		}
	}()

	// 🔌 Activate Persistent Event Stream Server
	go rpc.StartWSServer(*wsPort, stateStore)

	rpc.StartRPCServer(*rpcPort)
}
