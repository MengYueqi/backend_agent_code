package test

import (
	"reflect"
	"testing"

	"go_coding_noalgorithm/src"
)

func cloneInts(nums []int) []int {
	if nums == nil {
		return nil
	}

	got := make([]int, len(nums))
	copy(got, nums)
	return got
}

func TestQuickSort(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			name: "basic case",
			nums: []int{5, 1, 4, 2, 8},
			want: []int{1, 2, 4, 5, 8},
		},
		{
			name: "contains duplicates",
			nums: []int{3, 1, 2, 3, 2},
			want: []int{1, 2, 2, 3, 3},
		},
		{
			name: "contains negative numbers",
			nums: []int{-3, 0, 2, -1, 5},
			want: []int{-3, -1, 0, 2, 5},
		},
		{
			name: "already sorted",
			nums: []int{1, 2, 3, 4, 5},
			want: []int{1, 2, 3, 4, 5},
		},
		{
			name: "reverse sorted",
			nums: []int{9, 7, 5, 3, 1},
			want: []int{1, 3, 5, 7, 9},
		},
		{
			name: "single element",
			nums: []int{7},
			want: []int{7},
		},
		{
			name: "empty slice",
			nums: []int{},
			want: []int{},
		},
		{
			name: "nil slice",
			nums: nil,
			want: nil,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := cloneInts(tt.nums)

			src.QuickSort(got)

			if !reflect.DeepEqual(got, tt.want) {
				t.Fatalf("QuickSort(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}

func TestHeapSort(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			name: "basic case",
			nums: []int{5, 1, 4, 2, 8},
			want: []int{1, 2, 4, 5, 8},
		},
		{
			name: "contains duplicates",
			nums: []int{3, 1, 2, 3, 2},
			want: []int{1, 2, 2, 3, 3},
		},
		{
			name: "contains negative numbers",
			nums: []int{-3, 0, 2, -1, 5},
			want: []int{-3, -1, 0, 2, 5},
		},
		{
			name: "already sorted",
			nums: []int{1, 2, 3, 4, 5},
			want: []int{1, 2, 3, 4, 5},
		},
		{
			name: "reverse sorted",
			nums: []int{9, 7, 5, 3, 1},
			want: []int{1, 3, 5, 7, 9},
		},
		{
			name: "single element",
			nums: []int{7},
			want: []int{7},
		},
		{
			name: "empty slice",
			nums: []int{},
			want: []int{},
		},
		{
			name: "nil slice",
			nums: nil,
			want: nil,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := cloneInts(tt.nums)

			src.HeapSort(got)

			if !reflect.DeepEqual(got, tt.want) {
				t.Fatalf("HeapSort(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}
