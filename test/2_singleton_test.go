package test

import (
	"sync"
	"testing"

	"go_coding_noalgorithm/src"
)

func TestGetInstance_NotNil(t *testing.T) {
	instance := src.GetInstance()
	if instance == nil {
		t.Fatal("expected non-nil singleton instance")
	}
}

func TestGetInstance_SamePointer(t *testing.T) {
	first := src.GetInstance()
	second := src.GetInstance()

	if first != second {
		t.Fatal("expected same singleton pointer across calls")
	}
}

func TestGetInstance_ConcurrentSamePointer(t *testing.T) {
	const goroutines = 100

	results := make([]*src.Singleton, goroutines)
	var wg sync.WaitGroup
	wg.Add(goroutines)

	for i := 0; i < goroutines; i++ {
		go func(idx int) {
			defer wg.Done()
			results[idx] = src.GetInstance()
		}(i)
	}
	wg.Wait()

	base := results[0]
	for i := 1; i < goroutines; i++ {
		if results[i] != base {
			t.Fatalf("expected all goroutines to get same singleton pointer, mismatch at index %d", i)
		}
	}
}
