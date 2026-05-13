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
	genesisPath := flag.String("genesis", "core/genesis.json", "Path to genesis config")
	rpcPort := flag.Int("rpc.port", 8545, "RPC Port")

	flag.Parse()

	if _, err := os.Stat(*genesisPath); err != nil {
		fmt.Println("Genesis file missing:", err)
		os.Exit(1)
	}

	fmt.Println("==================================================")
	fmt.Println("STG SOVEREIGN NODE BOOTING (ENVIRONMENT: USERLAND)")
	fmt.Println("==================================================")
	fmt.Println("Genesis Loaded:", *genesisPath)
	fmt.Println("RPC Port:", *rpcPort)

	stateStore := core.NewStateDB()

	// ⛏️ Live Async Mining & Aksara Parameter Telemetry
	go func() {
		for {
			time.Sleep(5 * time.Second)
			stateStore.IncrementBlock()
			
			rawBlockStr := fmt.Sprintf("BLOCK:%d", stateStore.GetBlock())
			aksaraSignature := stateStore.EncryptStringToAksara(rawBlockStr)

			fmt.Println("--------------------------------------------------")
			fmt.Printf("⛏️  New Block Mined  : %d\n", stateStore.GetBlock())
			fmt.Printf("🔐 Aksara Telemetry : %s\n", aksaraSignature)
			fmt.Println("--------------------------------------------------")
		}
	}()

	rpc.StartRPCServer(*rpcPort, stateStore)
}
