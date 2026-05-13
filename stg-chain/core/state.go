package core

import (
	"crypto/sha256"
	"encoding/binary"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"log"
	"strings"
	"sync"
	"time"

	"github.com"
)

type Transaction struct {
	Hash  string `json:"hash"`
	From  string `json:"from"`
	To    string `json:"to"`
	Value uint64 `json:"value"`
}

type StateDB struct {
	mu        sync.RWMutex
	db        *leveldb.DB
	CipherMap map[string]string
}

func NewStateDB(dbPath string) *StateDB {
	db, err := leveldb.OpenFile(dbPath, nil)
	if err != nil {
		log.Fatalf("Fatal: Failed to open LevelDB at %s: %v", dbPath, err)
	}

	s := &StateDB{
		db:        db,
		CipherMap: make(map[string]string),
	}

	// Initialize Level 2 Aksara-Logic Encryption Matrix
	s.CipherMap["0"] = "꧐"
	s.CipherMap["1"] = "꧑"
	s.CipherMap["2"] = "꧒"
	s.CipherMap["3"] = "꧓"
	s.CipherMap["4"] = "꧔"
	s.CipherMap["5"] = "꧕"
	s.CipherMap["6"] = "꧖"
	s.CipherMap["7"] = "꧗"
	s.CipherMap["8"] = "꧘"
	s.CipherMap["9"] = "꧙"
	s.CipherMap["A"] = "ꦄ"
	s.CipherMap["B"] = "ꦧ"
	s.CipherMap["C"] = "ꦼ"
	s.CipherMap["D"] = "ꦢ"
	s.CipherMap["E"] = "ꦌ"
	s.CipherMap["X"] = "ꦏꦱ"

	// Initialize state balances if database is blank
	if _, err := s.db.Get([]byte("blk:latest"), nil); err != nil {
		s.SetBlock(1)
		s.SetBalance("0xgenesis", 1000000)
	}

	return s
}

func (s *StateDB) SetBlock(num uint64) {
	b := make([]byte, 8)
	binary.BigEndian.PutUint64(b, num)
	_ = s.db.Put([]byte("blk:latest"), b, nil)
}

func (s *StateDB) GetBlock() uint64 {
	b, err := s.db.Get([]byte("blk:latest"), nil)
	if err != nil {
		return 1
	}
	return binary.BigEndian.Uint64(b)
}

func (s *StateDB) IncrementBlock() {
	s.mu.Lock()
	defer s.mu.Unlock()
	next := s.GetBlock() + 1
	s.SetBlock(next)
}

func (s *StateDB) SetBalance(addr string, amount uint64) {
	b := make([]byte, 8)
	binary.BigEndian.PutUint64(b, amount)
	_ = s.db.Put([]byte("bal:"+addr), b, nil)
}

func (s *StateDB) GetBalance(addr string) uint64 {
	b, err := s.db.Get([]byte("bal:"+addr), nil)
	if err != nil {
		return 0
	}
	return binary.BigEndian.Uint64(b)
}

func (s *StateDB) SendTransaction(from string, to string, value uint64) (string, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	balFrom := s.GetBalance(from)
	if balFrom < value {
		return "", fmt.Errorf("insufficient funds")
	}

	s.SetBalance(from, balFrom-value)
	s.SetBalance(to, s.GetBalance(to)+value)

	raw := fmt.Sprintf("%s:%s:%d:%d", from, to, value, time.Now().UnixNano())
	hash := sha256.Sum256([]byte(raw))
	txHash := "0x" + hex.EncodeToString(hash[:])

	tx := Transaction{Hash: txHash, From: from, To: to, Value: value}
	txData, _ := json.Marshal(tx)

	// Save individual transaction record and index it under global slice registry
	_ = s.db.Put([]byte("tx:"+txHash), txData, nil)
	
	var txList []string
	if listData, err := s.db.Get([]byte("tx:registry"), nil); err == nil {
		json.Unmarshal(listData, &txList)
	}
	txList = append(txList, txHash)
	newListData, _ := json.Marshal(txList)
	_ = s.db.Put([]byte("tx:registry"), newListData, nil)

	return txHash, nil
}

func (s *StateDB) GetTransactions() []Transaction {
	var txList []string
	var txRecords []Transaction
	
	listData, err := s.db.Get([]byte("tx:registry"), nil)
	if err != nil {
		return txRecords
	}
	json.Unmarshal(listData, &txList)

	for _, hash := range txList {
		if txData, err := s.db.Get([]byte("tx:"+hash), nil); err == nil {
			var tx Transaction
			json.Unmarshal(txData, &tx)
			txRecords = append(txRecords, tx)
		}
	}
	return txRecords
}

func (s *StateDB) EncryptStringToAksara(input string) string {
	upperInput := strings.ToUpper(input)
	var output []string
	for _, char := range upperInput {
		strChar := string(char)
		if val, exists := s.CipherMap[strChar]; exists {
			output = append(output, val)
		} else {
			output = append(output, strChar)
		}
	}
	return strings.Join(output, "")
}

func (s *StateDB) Close() {
	s.db.Close()
}
