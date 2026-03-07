package test

import (
	"testing"

	"go_coding_noalgorithm/src"
)

func TestMaxLenAtMostTwoDistinct(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "empty",
			nums: []int{},
			want: 0,
		},
		{
			name: "single",
			nums: []int{7},
			want: 1,
		},
		{
			name: "all same",
			nums: []int{5, 5, 5, 5},
			want: 4,
		},
		{
			name: "exactly two distinct",
			nums: []int{1, 2, 1, 2, 1},
			want: 5,
		},
		{
			name: "classic case one",
			nums: []int{1, 2, 3, 2, 2},
			want: 4,
		},
		{
			name: "classic case two",
			nums: []int{1, 2, 1, 1, 3},
			want: 4,
		},
		{
			name: "drop left side when third appears",
			nums: []int{0, 1, 2, 2},
			want: 3,
		},
		{
			name: "with negative numbers",
			nums: []int{-1, -1, -2, -3, -3, -2, -2},
			want: 5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := src.MaxLenAtMostTwoDistinct(tt.nums)
			if got != tt.want {
				t.Fatalf("nums=%v want=%d got=%d", tt.nums, tt.want, got)
			}
		})
	}
}
