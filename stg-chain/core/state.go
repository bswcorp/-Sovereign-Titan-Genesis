package core

import (
	"sync"
)

type StateDB struct {
	mu          sync.RWMutex
	CurrentBlock uint64
}

func NewStateDB() *StateDB {
	return &StateDB{
		CurrentBlock: 1,
	}
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
