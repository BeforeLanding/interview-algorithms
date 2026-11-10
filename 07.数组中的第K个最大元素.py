"""215. 数组中的第 K 个最大元素
题目：https://leetcode.cn/problems/kth-largest-element-in-an-array/
题意：返回降序排列后第 k 个元素，重复元素也参与排名。

思路：第 k 大对应升序下标 n-k。随机选基准，将当前区间划分为两部分，
定位基准的最终下标，只继续查找含目标下标的一侧，无需排好整个数组。
使用左右指针交换：遇到等于基准的数也会向内移动，避免全相等时反复只缩小一格。
平均时间 O(n)，最坏 O(n²)，额外空间 O(1)。会原地重排 nums。
易错：目标下标是 n-k；k 必须满足 1 <= k <= len(nums)。

参考：灵茶山艾府，随机快速选择及重复值处理思路；此处独立整理实现与讲解。
原文页面读取受限，已核实题解链接与标题。
https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/3799769/on-kuai-su-xuan-ze-suan-fa-pythonjavaccg-lh7c/
"""

from random import randint


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_index = randint(left, right)
            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            pivot = nums[left]
            i, j = left + 1, right
            while True:
                while i <= j and nums[i] < pivot:
                    i += 1
                while i <= j and nums[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            nums[left], nums[j] = nums[j], nums[left]
            if j == target:
                return nums[j]
            if j < target:
                left = j + 1
            else:
                right = j - 1
        raise ValueError("k 必须满足 1 <= k <= len(nums)")


if __name__ == "__main__":
    solution = Solution()
    assert solution.findKthLargest([7, 2, 9, 4, 7], 2) == 7
    assert solution.findKthLargest([3, 3, 3, 3], 3) == 3
    assert solution.findKthLargest([-3, -1, -2], 1) == -1
    assert solution.findKthLargest([1], 1) == 1
    print("215. 数组中的第 K 个最大元素：通过")
