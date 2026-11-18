"""15. 三数之和
题目：https://leetcode.cn/problems/3sum/
题意：找出和为 0 的所有不重复三元组，三个元素的下标必须不同。

思路
为方便双指针以及跳过相同元素，先把 nums 排序。

枚举 nums[i]，问题变成 nums[j]+nums[k]=−nums[i]，这和 167. 两数之和 II - 输入有序数组 是一样的。

题目要求答案中不能有重复的三元组。如何避免重复？

在外层循环中，如果发现 nums[i]=nums[i−1]，那么 nums[i] 与后面两个数组成的和为 0 的三元组，nums[i−1] 也能组成一模一样的三元组，这就重复了，所以遇到 nums[i]=nums[i−1] 的情况，直接 continue。

在内层循环中，当三数之和等于 0 时，为避免把相同的三元组计入答案，跳过后续相同的 nums[j] 和 nums[k]（也可以只跳过相同的 nums[j]）。

优化
优化一：如果 nums[i] 与后面最小的两个数相加 nums[i]+nums[i+1]+nums[i+2]>0，那么后面不可能存在三数之和等于 0，break 外层循环。

优化二：如果 nums[i] 与后面最大的两个数相加 nums[i]+nums[n−2]+nums[n−1]<0，那么内层循环不可能存在三数之和等于 0，但继续枚举，nums[i] 可以变大，所以后面还有机会找到三数之和等于 0，continue 外层循环。

时间复杂度：O(n2)，其中 n 为 nums 的长度。排序 O(nlogn)。外层循环枚举第一个数，就变成 167. 两数之和 II - 输入有序数组 了，做法是 O(n) 双指针。所以总的时间复杂度为 O(n2)。
空间复杂度：O(1)。返回值不计入。忽略排序的栈开销。
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:  # 跳过重复数字
                continue
            if x + nums[i + 1] + nums[i + 2] > 0:  # 优化一
                break
            if x + nums[-2] + nums[-1] < 0:  # 优化二
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:  # 三数之和为 0
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:  # 跳过重复数字
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:  # 跳过重复数字
                        k -= 1
        return ans
