"""215. 数组中的第 K 个最大元素
题目：https://leetcode.cn/problems/kth-largest-element-in-an-array/
题意：返回降序排列后第 k 个元素，重复元素也参与排名。

思路：第 k 大对应升序下标 n-k。随机选基准，将当前区间划分为两部分，
定位基准的最终下标，只继续查找含目标下标的一侧，无需排好整个数组。
使用左右指针交换：遇到等于基准的数也会向内移动，避免全相等时反复只缩小一格。

平均时间 O(n)，最坏 O(n²)，
额外空间 O(1)。会原地重排 nums。
"""

class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        """
        在子数组 [left, right] 中随机选择一个基准元素 pivot
        根据 pivot 重新排列子数组 [left, right]
        重新排列后，<= pivot 的元素都在 pivot 的左侧，>= pivot 的元素都在 pivot 的右侧
        返回 pivot 在重新排列后的 nums 中的下标
        特别地，如果子数组的所有元素都等于 pivot，我们会返回子数组的中心下标，避免退化
        """

        # 1. 在子数组 [left, right] 中随机选择一个基准元素 pivot
        i = randint(left, right)
        pivot = nums[i]
        # 把 pivot 与子数组第一个元素交换，避免 pivot 干扰后续划分，从而简化实现逻辑
        nums[i], nums[left] = nums[left], nums[i]

        # 2. 相向双指针遍历子数组 [left + 1, right]
        # 循环不变量：在循环过程中，子数组的数据分布始终如下图
        # [ pivot | <=pivot | 尚未遍历 | >=pivot ]
        #   ^                 ^     ^         ^
        #   left              i     j         right

        i, j = left + 1, right
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            # 此时 nums[i] >= pivot

            while i <= j and nums[j] > pivot:
                j -= 1
            # 此时 nums[j] <= pivot

            if i >= j:
                break

            # 维持循环不变量
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # 循环结束后
        # [ pivot | <=pivot | >=pivot ]
        #   ^             ^   ^     ^
        #   left          j   i     right

        # 3. 把 pivot 与 nums[j] 交换，完成划分（partition）
        # 为什么与 j 交换？
        # 如果与 i 交换，可能会出现 i = right + 1 的情况，已经下标越界了，无法交换
        # 另一个原因是如果 nums[i] > pivot，交换会导致一个大于 pivot 的数出现在子数组最左边，不是有效划分
        # 与 j 交换，即使 j = left，交换也不会出错
        nums[left], nums[j] = nums[j], nums[left]

        # 交换后
        # [ <=pivot | pivot | >=pivot ]
        #               ^
        #               j

        # 返回 pivot 的下标
        return j

    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        target_index = n - k  # 第 k 大元素在升序数组中的下标是 n - k
        left, right = 0, n - 1  # 闭区间
        while True:
            i = self.partition(nums, left, right)
            if i == target_index:
                # 找到第 k 大元素
                return nums[i]
            if i > target_index:
                # 第 k 大元素在 [left, i - 1] 中
                right = i - 1
            else:
                # 第 k 大元素在 [i + 1, right] 中
                left = i + 1
