package src

// MaxLenAtMostTwoDistinct returns the max length of a contiguous subarray
// containing at most two distinct numbers.
func MaxLenAtMostTwoDistinct(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	maxLen := 0
	first, last := 0, 0
	helpHash := make(map[int]int, 0)
	for last < len(nums) {
		helpHash[nums[last]]++
		if len(helpHash) > 2 {
			for len(helpHash) > 2 {
				helpHash[nums[first]]--
				if helpHash[nums[first]] == 0 {
					delete(helpHash, nums[first])
				}
				first++
			}
			maxLen = max(maxLen, last-first+1)
			last++
		} else {
			maxLen = max(maxLen, last-first+1)
			last++
		}
	}
	return maxLen
}
