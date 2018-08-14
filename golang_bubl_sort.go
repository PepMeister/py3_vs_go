package main

import (
	"C"
	"fmt"
	"github.com/sbwhitecap/tqdm"
	. "github.com/sbwhitecap/tqdm/iterators"
	"math/rand"
)

//export arr_sorting
func arr_sorting(arr_size int) {
	x := make([]byte, arr_size)
	rand.Read(x)
	fmt.Println("before sorting: ", x[0:5], "...", x[arr_size-6:arr_size-1])

	end := len(x) - 1

	tqdm.With(Interval(0, len(x)-1), "sort:", func(v interface{}) (brk bool) {

		for i := 0; i < len(x)-1; i++ {
			if x[i] > x[i+1] {
				x[i], x[i+1] = x[i+1], x[i]
			}
		}
		end -= 1

		return
	})
	fmt.Println("after sorting:  ", x[0:5], "...", x[arr_size-6:arr_size-1])
}

func main() {}
