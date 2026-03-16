package test

import (
	"testing"

	"go_coding_noalgorithm/src"
)

func TestHasOneLetterDifference(t *testing.T) {
	tests := []struct {
		name  string
		words []string
		x     string
		want  bool
	}{
		{
			name:  "match by replacing one character",
			words: []string{"hello", "world"},
			x:     "hhllo",
			want:  true,
		},
		{
			name:  "exact same word does not count",
			words: []string{"hello", "world"},
			x:     "hello",
			want:  false,
		},
		{
			name:  "different length cannot match",
			words: []string{"abcd", "xy"},
			x:     "abc",
			want:  false,
		},
		{
			name:  "multiple candidates any one match is enough",
			words: []string{"judge", "badge", "ledge"},
			x:     "budge",
			want:  true,
		},
		{
			name:  "needs more than one replacement",
			words: []string{"abc", "def"},
			x:     "axf",
			want:  false,
		},
		{
			name:  "empty dictionary",
			words: []string{},
			x:     "abc",
			want:  false,
		},
		{
			name:  "single character word can match",
			words: []string{"a", "b"},
			x:     "c",
			want:  true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := src.HasOneLetterDifference(tt.words, tt.x)
			if got != tt.want {
				t.Fatalf("HasOneLetterDifference(%v, %q) = %v, want %v", tt.words, tt.x, got, tt.want)
			}
		})
	}
}
