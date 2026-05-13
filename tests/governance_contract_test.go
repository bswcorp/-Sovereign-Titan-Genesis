package tests

import (
    "testing"
)

// Mock internal structure for simulation before code-link
type MultiSigContract struct {
    Council   []string
    Threshold int
    Signs     map[string]bool
}

func NewMultiSigContract(council []string, threshold int) *MultiSigContract {
    return &MultiSigContract{Council: council, Threshold: threshold, Signs: make(map[string]bool)}
}

func (m *MultiSigContract) Sign(val string) { m.Signs[val] = true }
func (m *MultiSigContract) HasQuorum() bool { return len(m.Signs) >= m.Threshold }
func (m *MultiSigContract) ExecuteProposal(prop string) bool { return m.HasQuorum() }

func TestMultiSigQuorumExecution(t *testing.T) {
    council := []string{"val1", "val2", "val3", "val4", "val5"}
    contract := NewMultiSigContract(council, 3) // 3-of-5 quorum

    contract.Sign("val1")
    contract.Sign("val2")
    contract.Sign("val3")

    if !contract.HasQuorum() {
        t.Errorf("Expected quorum reached with 3 signatures")
    }
    if !contract.ExecuteProposal("Community Fund Allocation") {
        t.Errorf("Expected proposal execution after quorum")
    }
}

func TestMultiSigInsufficientQuorum(t *testing.T) {
    council := []string{"val1", "val2", "val3", "val4", "val5"}
    contract := NewMultiSigContract(council, 3)

    contract.Sign("val1")
    contract.Sign("val2")

    if contract.HasQuorum() {
        t.Errorf("Quorum should not be reached with only 2 signatures")
    }
    if contract.ExecuteProposal("Invalid Proposal") {
        t.Errorf("Proposal should not execute without quorum")
    }
}
