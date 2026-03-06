package test

import (
	"bytes"
	"io"
	"os"
	"strings"
	"testing"

	"go_coding_noalgorithm/src"
)

func captureStdout(t *testing.T, fn func()) string {
	t.Helper()

	oldStdout := os.Stdout
	r, w, err := os.Pipe()
	if err != nil {
		t.Fatalf("failed to create pipe: %v", err)
	}

	os.Stdout = w
	fn()

	_ = w.Close()
	os.Stdout = oldStdout

	var buf bytes.Buffer
	if _, err := io.Copy(&buf, r); err != nil {
		t.Fatalf("failed to read stdout: %v", err)
	}
	_ = r.Close()

	return buf.String()
}

func TestPrintABC_OrderAndCount(t *testing.T) {
	got := captureStdout(t, func() {
		src.PrintABC(3)
	})

	want := "a\nb\nc\na\nb\nc\na\nb\nc\n"
	if got != want {
		t.Fatalf("unexpected output\nwant:\n%q\ngot:\n%q", want, got)
	}
}

func TestPrintABC_Zero(t *testing.T) {
	got := captureStdout(t, func() {
		src.PrintABC(0)
	})

	if strings.TrimSpace(got) != "" {
		t.Fatalf("expected empty output when n=0, got %q", got)
	}
}
