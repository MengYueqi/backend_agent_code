package src

import (
	"fmt"
	"sync"
)

func PrintABC(n int) {
	ch1 := make(chan struct{}, 1)
	ch2 := make(chan struct{}, 1)
	ch3 := make(chan struct{}, 1)
	var wg sync.WaitGroup

	ch1 <- struct{}{}
	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 0; i < n; i++ {
			<-ch1
			fmt.Println("a")
			ch2 <- struct{}{}
		}
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 0; i < n; i++ {
			<-ch2
			fmt.Println("b")
			ch3 <- struct{}{}
		}
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 0; i < n; i++ {
			<-ch3
			fmt.Println("c")
			ch1 <- struct{}{}
		}
	}()

	wg.Wait()
}
