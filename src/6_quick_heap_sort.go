package src

// 题目：实现快排和堆排

func partition(nums []int, left, right int) {
	if left >= right {
		return
	}
	pivot := nums[left]
	first, last := left+1, right
	for {
		for first <= last && nums[first] <= pivot {
			first++
		}
		for first <= last && nums[last] >= pivot {
			last--
		}
		if first >= last {
			break
		}
		nums[first], nums[last] = nums[last], nums[first]
	}
	nums[left], nums[last] = nums[last], nums[left]
	partition(nums, left, last-1)
	partition(nums, last+1, right)
}

func QuickSort(nums []int) {
	// TODO: implement quick sort
	partition(nums, 0, len(nums)-1)
}

func siftDown(nums []int, node, last int) {
	for {
		child := node*2 + 1
		if child > last {
			break
		}
		next := node
		if nums[node] < nums[child] {
			next = child
		}
		if child+1 <= last && nums[next] < nums[child+1] {
			next = child + 1
		}
		if next == node {
			return
		} else {
			nums[node], nums[next] = nums[next], nums[node]
			node = next
		}
	}
}

func HeapSort(nums []int) {
	// TODO: implement heap sort
	for i := len(nums) / 2; i >= 0; i-- {
		siftDown(nums, i, len(nums)-1)
	}

	for i := len(nums) - 1; i >= 0; i-- {
		nums[0], nums[i] = nums[i], nums[0]
		siftDown(nums, 0, i-1)
	}

}
