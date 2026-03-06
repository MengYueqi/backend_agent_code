package src

import "sync"

type Singleton struct {
	value int
}

var singleton *Singleton
var once sync.Once

func GetInstance() *Singleton {
	once.Do(func() {
		singleton = &Singleton{
			value: 6,
		}
	},
	)
	return singleton
}
