package main

import (
	"C"
	"fmt"
	"math/rand"
)

//export  small_arr_sorting
func small_arr_sorting() {
	x := []int{5, 2, 7, 4, 0, 9, 8, 6}
	fmt.Println("before sorting: ", x)
	end := len(x) - 1

	for {
		if end == 0 {
			break
		}
		for i := 0; i < len(x)-1; i++ {
			if x[i] > x[i+1] {
				x[i], x[i+1] = x[i+1], x[i]
			}
		}
		end -= 1
	}
	fmt.Println("after sorting:  ", x)
}

//export big_arr_sorting
func big_arr_sorting(arr_size int) {
	x := make([]byte, arr_size)
	rand.Read(x)
	fmt.Println("before sorting: ", x[0:5], "...", x[arr_size-6:arr_size-1])

	end := len(x) - 1

	for {
		if end == 0 {
			break
		}
		for i := 0; i < len(x)-1; i++ {
			if x[i] > x[i+1] {
				x[i], x[i+1] = x[i+1], x[i]
			}
		}
		end -= 1
	}
	fmt.Println("after sorting:  ", x[0:5], "...", x[arr_size-6:arr_size-1])
}

func main() {}
