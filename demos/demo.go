// Package declaration
package main

// Imports: Standard and Aliased
import (
	"context"
	"errors"
	"fmt"
	m "math" // Alias import
	"sync"
	"time"
)

// ----------------------------------------------------------------------------
// 1. Constants, Variables & Basic Types
// ----------------------------------------------------------------------------

// Block declaration with iota
const (
	StatusIdle = iota
	StatusRunning
	StatusStopped
	// Arithmetic in constants
	StatusError = 1 << 4
)

// Primitive types
var (
	isActive  bool       = true
	intHex    int        = 0xFF_00 // Hex with separator
	floatVal  float64    = 3.14159
	complexNo complex128 = 5 + 10i
	ptr       *int       = nil
)

// String Literals
const (
	rawString    = `This is a raw string literal \n (backticks)`
	escapedString = "Line 1\nLine 2\tTabbed \"Quote\""
)

// ----------------------------------------------------------------------------
// 2. Structs & Interfaces & Tags
// ----------------------------------------------------------------------------

// Interface definition
type Shape interface {
	Area() float64
	// Embedded interface
	fmt.Stringer
}

// Struct definition with Tags (Important for highlighting)
type Circle struct {
	// Public field
	Radius float64 `json:"radius" xml:"radius,attr" binding:"required"`
	// Private field
	center struct {
		x, y int
	}
}

// Method receiver (Pointer vs Value)
func (c *Circle) Area() float64 {
	return m.Pi * c.Radius * c.Radius
}

func (c Circle) String() string {
	return fmt.Sprintf("Circle(r=%.2f)", c.Radius)
}

// ----------------------------------------------------------------------------
// 3. Generics (Go 1.18+)
// ----------------------------------------------------------------------------

// Generic Constraint
type Number interface {
	int64 | float64
}

// Generic Struct
type Cache[K comparable, V any] struct {
	data map[K]V
	mu   sync.RWMutex
}

// Generic Function
func Sum[T Number](numbers []T) T {
	var total T
	for _, x := range numbers {
		total += x
	}
	return total
}

// ----------------------------------------------------------------------------
// 4. Control Flow & Functions
// ----------------------------------------------------------------------------

// Function with named return values and Variadic parameters
func calculate(base int, ops ...string) (result int, err error) {
	// Defer statement
	defer func() {
		if r := recover(); r != nil {
			err = errors.New("recovered from panic")
		}
	}()

	result = base

	// Control Structures
	for i, op := range ops {
		if i == 0 {
			continue
		}

		switch op {
		case "inc":
			result++
		case "dec":
			result--
		default:
			// Fallthrough logic
			fallthrough
		case "unknown":
			return 0, fmt.Errorf("unknown op: %s", op)
		}
	}

	if result < 0 {
		panic("negative result")
	}

	return result, nil
}

// ----------------------------------------------------------------------------
// 5. Concurrency (Goroutines & Channels)
// ----------------------------------------------------------------------------

func worker(ctx context.Context, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		select {
		case <-ctx.Done():
			return
		case results <- j * 2:
			// Sent successfully
		}
	}
}

// ----------------------------------------------------------------------------
// 6. Main Execution Block
// ----------------------------------------------------------------------------

func main() {
	// Short declaration
	c := &Circle{Radius: 5.5}

	// Type Assertion
	var s interface{} = c
	if circle, ok := s.(*Circle); ok {
		fmt.Println(circle.Area())
	}

	// Type Switch
	switch v := s.(type) {
	case *Circle:
		fmt.Printf("It's a circle: %v\n", v)
	case int:
		fmt.Println("Integer")
	default:
		fmt.Println("Unknown")
	}

	// Generic usage
	ints := []int64{1, 2, 3, 4}
	sum := Sum(ints)
	fmt.Printf("Sum: %d\n", sum)

	// Built-in functions
	slice := make([]int, 0, 10)
	slice = append(slice, 1)
	length := len(slice)
	_ = new(int) // Allocates

	// Map initialization
	lookup := map[string]int{
		"one": 1,
		"two": 2,
	}
	delete(lookup, "one")

	fmt.Println("Done", length)
}
