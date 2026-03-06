package main

import (
	"go_coding_noalgorithm/src"
)

func main() {
	src.PrintABC(3)
	// PrintABC currently launches goroutines and returns immediately.
	// time.Sleep(200 * time.Millisecond)
}
