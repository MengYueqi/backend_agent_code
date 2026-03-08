package test

import (
	"testing"

	"go_coding_noalgorithm/src"
)

func TestBuildMaxLessThanN(t *testing.T) {
	tests := []struct {
		name   string
		n      int
		digits []int
		want   int
	}{
		{
			name:   "basic case",
			n:      345,
			digits: []int{1, 3, 5},
			want:   335,
		},
		{
			name:   "need backtrack in same length",
			n:      572,
			digits: []int{2, 5, 7},
			want:   557,
		},
		{
			name:   "fall back to shorter length",
			n:      1000,
			digits: []int{0, 1},
			want:   111,
		},
		{
			name:   "single digit only",
			n:      21,
			digits: []int{2},
			want:   2,
		},
		{
			name:   "zero is valid result",
			n:      10,
			digits: []int{0},
			want:   0,
		},
		{
			name:   "no solution",
			n:      1,
			digits: []int{9},
			want:   -1,
		},
		{
			name:   "n equals zero",
			n:      0,
			digits: []int{0, 1, 2},
			want:   -1,
		},
		{
			name:   "deduplicate digits",
			n:      332,
			digits: []int{3, 3, 1},
			want:   331,
		},
		{
			name:   "leading zero not allowed except zero itself",
			n:      100,
			digits: []int{0, 1},
			want:   11,
		},
		{
			name:   "empty digits",
			n:      999,
			digits: []int{},
			want:   -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := src.BuildMaxLessThanN(tt.n, tt.digits)
			if got != tt.want {
				t.Fatalf("n=%d digits=%v want=%d got=%d", tt.n, tt.digits, tt.want, got)
			}
		})
	}
}
