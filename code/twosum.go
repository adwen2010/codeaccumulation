package main

import "fmt"

func twoSumtest() {
	arr := []int{1, 2, 3, 5}
	fmt.Println(twoSum(arr, 5))
	fmt.Println(twoSum2(arr, 5))
}

func twoSum(nums []int, target int) []int {
	res := make([]int, 0)
	mm := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		mm[nums[i]] = i
	}
	for i := 0; i < len(nums); i++ {
		k, ok := mm[target-nums[i]]
		if ok == true && i != k {
			res = append(res, i, k)
			break
		}
	}
	return res
}
func twoSum2(nums []int, target int) []int {
	res := make([]int, 0)
	mm := make(map[int]int)
	//for i := 0; i < len(nums); i++ {
	//	mm[nums[i]] = i
	//}
	for i := 0; i < len(nums); i++ {
		k, ok := mm[target-nums[i]]
		if ok == true && i != k {
			res = append(res, k, i)
			break
		}
		mm[nums[i]] = i
	}
	return res
}
