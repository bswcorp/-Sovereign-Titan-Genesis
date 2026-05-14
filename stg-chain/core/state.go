package core

import (
	"sync"
)

type StateDB struct {
	mu        sync.RWMutex
	balances  map[string]uint64
	latestBlk uint64
}

func NewStateDB() *StateDB {
	db := &StateDB{
		balances:  make(map[string]uint64),
		latestBlk: 1,
	}
	// Kunci Saldo Awal Sultan (100 Juta Token Utama)
	db.balances["0x3AA63941Fe0Ce029f4523c57A30C6dca3cB7343F"] = 100000000000000000
	return db
}

func (s *StateDB) GetBalance(address string) uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.balances[address]
}

func (s *StateDB) IncrementBlock() {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.latestBlk++
}

func (s *StateDB) GetLatestBlock() uint64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.latestBlk
}
