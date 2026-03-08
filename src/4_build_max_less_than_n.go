package src

import "sort"

func findSame(n int, nums []int) bool {
	for i := 0; i < len(nums); i++ {
		if n == nums[i] {
			return true
		}
	}
	return false
}

func findSmall(n int, nums []int) bool {
	for i := 0; i < len(nums); i++ {
		if n > nums[i] {
			return true
		}
	}
	return false
}

func BuildMaxLessThanN(n int, digits []int) int {
	// TODO: implement
	if n < 10 && !findSmall(n, digits) || len(digits) == 0 {
		return -1
	}
	n -= 1
	nums := make([]int, 0)
	for n != 0 {
		nums = append([]int{n % 10}, nums...)
		n = n / 10
	}
	idx := 0
	sort.Ints(digits)
	res := make([]int, len(nums))
	for idx < len(nums) {
		if findSame(nums[idx], digits) {
			res[idx] = nums[idx]
			idx++
		} else if findSmall(nums[idx], digits) {
			curNum := 0
			for i := 0; i < len(digits); i++ {
				if digits[i] < nums[idx] {
					curNum = max(curNum, digits[i])
				}
			}
			res[idx] = curNum
			idx++
			for idx < len(nums) {
				res[idx] = digits[len(digits)-1]
				idx++
			}
			break
		} else {
			// 回溯逻辑
			idx--
			for idx >= 0 && !findSmall(nums[idx], digits) {
				idx--
			}
			if idx < 0 {
				res[0] = 0
				for i := 1; i < len(res); i++ {
					res[i] = digits[len(digits)-1]
				}
			} else {
				curNum := 0
				for i := 0; i < len(digits); i++ {
					if digits[i] < nums[idx] {
						curNum = max(curNum, digits[i])
					}
				}
				res[idx] = curNum
				idx++
				for idx < len(nums) {
					res[idx] = digits[len(digits)-1]
					idx++
				}
			}
			break
		}
	}
	resNum := 0

	for i := 0; i < len(res); i++ {
		resNum = resNum*10 + res[i]
	}

	return resNum
}
