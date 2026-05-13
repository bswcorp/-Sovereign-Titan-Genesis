package main

import (
	"flag"
	"fmt"
	"os"

	"stg-chain/core"
	"stg-chain/rpc"
)

func main() {

	genesisPath := flag.String(
		"genesis",
		"core/genesis.json",
		"path to genesis config",
	)

	rpcPort := flag.Int(
		"rpc.port",
		8545,
		"json rpc port",
	)

	validatorMode := flag.Bool(
		"validator",
		false,
		"enable validator mode",
	)

	flag.Parse()

	fmt.Println("--------------------------------------------------")
	fmt.Println("STG CHAIN NODE INITIALIZATION")
	fmt.Println("--------------------------------------------------")

	_, err := os.ReadFile(*genesisPath)
	if err != nil {
		fmt.Println("failed to load genesis:", err)
		os.Exit(1)
	}

	fmt.Println("genesis loaded from:", *genesisPath)
	fmt.Println("rpc port:", *rpcPort)
	fmt.Println("validator mode:", *validatorMode)

	stateStore := core.NewStateDB()

	stateStore.SetBalance(
		"0x3AA63941Fe0Ce029f4523c57A30C6dca3cB7343F",
		1000000000,
	)

	go func() {
		for {
			stateStore.IncrementBlock()
		}
	}()

	rpc.StartRPCServer(*rpcPort, stateStore)
}
