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
	genesisPath := flag.String(
		"genesis",
		"core/genesis.json",
		"Path to genesis config",
	)

	rpcPort := flag.Int(
		"rpc.port",
		8545,
		"RPC Port",
	)

	flag.Parse()

	if _, err := os.Stat(*genesisPath); err != nil {
		fmt.Println("Genesis file missing:", err)
		os.Exit(1)
	}

	fmt.Println("STG Sovereign Node Booting")
	fmt.Println("Genesis Loaded:", *genesisPath)
	fmt.Println("RPC Port:", *rpcPort)

	stateStore := core.NewStateDB()

	// ⛏️ Fake Mining Loop
	go func() {
		for {
			time.Sleep(5 * time.Second)
			stateStore.IncrementBlock()
			fmt.Println("⛏️ New Block Mined:", stateStore.GetBlock())
		}
	}()

	rpc.StartRPCServer(*rpcPort, stateStore)
}
