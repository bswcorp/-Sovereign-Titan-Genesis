package core

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"sync"
	"time"
)

type Transaction struct {
	Hash  string `json:"hash"`
	From  string `json:"from"`
	To    string `json:"to"`
	Value uint64 `json:"value"`
}

type StateDB struct {
	mu           sync.RWMutex
	CurrentBlock uint64
	Balances     map[string]uint64
	Transactions []Transaction
}

func NewStateDB() *StateDB {
	s := &StateDB{
		CurrentBlock: 1,
		Balances:     make(map[string]uint64),
		Transactions: []Transaction{},
	}

	// Genesis Wallet
	s.Balances["0xgenesis"] = 1000000
	return s
}

func (s *StateDB) IncrementBlock() {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.CurrentBlock++
}

func (s *StateDB) GetBlock() uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.CurrentBlock
}

func (s *StateDB) GetBalance(addr string) uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.Balances[addr]
}

func (s *StateDB) SendTransaction(from string, to string, value uint64) (string, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	if s.Balances[from] < value {
		return "", fmt.Errorf("insufficient funds")
	}

	s.Balances[from] -= value
	s.Balances[to] += value

	raw := fmt.Sprintf("%s:%s:%d:%d", from, to, value, time.Now().UnixNano())
	hash := sha256.Sum256([]byte(raw))
	txHash := "0x" + hex.EncodeToString(hash[:])

	tx := Transaction{
		Hash:  txHash,
		From:  from,
		To:    to,
		Value: value,
	}

	s.Transactions = append(s.Transactions, tx)
	return txHash, nil
}

func (s *StateDB) GetTransactions() []Transaction {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.Transactions
}
