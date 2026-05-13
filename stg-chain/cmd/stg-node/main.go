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
	rpcPort := flag.Int("rpc.port", 8545, "HTTP RPC Port")
	wsPort := flag.Int("ws.port", 8546, "WebSocket Stream Port")

	flag.Parse()

	if _, err := os.Stat(*genesisPath); err != nil {
		fmt.Println("Genesis file missing:", err)
		os.Exit(1)
	}

	fmt.Println("==================================================")
	fmt.Println("STG SOVEREIGN NODE BOOTING (ENGINE: LEVELDB + WS)")
	fmt.Println("==================================================")

	// Instantiating LevelDB Binary Engine directory layout
	stateStore := core.NewStateDB("core/state_leveldb")
	defer stateStore.Close()

	go func() {
		for {
			time.Sleep(5 * time.Second)
			stateStore.IncrementBlock()
			
			rawBlockStr := fmt.Sprintf("BLOCK:%d", stateStore.GetBlock())
			aksaraSignature := stateStore.EncryptStringToAksara(rawBlockStr)

			fmt.Printf("⛏️  Block: %d | 🔐 Aksara: %s\n", stateStore.GetBlock(), aksaraSignature)

			// Push native block update events dynamically through WebSocket connections
			rpc.BroadcastEvent(map[string]interface{}{
				"event": "new_block",
				"block": stateStore.GetBlock(),
				"aksara": aksaraSignature,
			})
		}
	}()

	rpc.StartRPCServer(*rpcPort, *wsPort, stateStore)
	
	// Keep process alive indefinitely
	select {}
}
