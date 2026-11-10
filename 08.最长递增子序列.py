"""300. 最长递增子序列
题目：https://leetcode.cn/problems/longest-increasing-subsequence/
题意：可以删除元素但不能改变顺序，求严格递增的最长子序列长度。

解法一：dp[i] 表示以 nums[i] 结尾的 LIS 长度，初值为 1。
枚举 j < i 且 nums[j] < nums[i]，用 dp[j] + 1 更新 dp[i]。
时间 O(n²)，空间 O(n)。适合先理解状态和转移。

解法二：tails[i] 表示长度为 i+1 的递增子序列，能达到的最小末尾值。
依次处理 x，二分找第一个 >= x 的位置并替换；若不存在，就接到末尾。
末尾越小，越容易接上后面的数。答案是 tails 的长度。
时间 O(n log n)，空间 O(n)。两个解法都不修改输入。
易错：严格递增用 bisect_left；tails 本身不一定是原数组的一个子序列。

参考：灵茶山艾府《三种方法：记忆化搜索/递推/二分查找》，基础算法精讲 20。
已从力扣索引核实作者和方法；正文读取受限，以下为独立整理。
https://leetcode.cn/problems/longest-increasing-subsequence/solutions/?envId=top-100-liked&envType=study-plan-v2
"""

from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for value in nums:
            i = bisect_left(tails, value)
            if i == len(tails):
                tails.append(value)
            else:
                tails[i] = value
        return len(tails)

    def lengthOfLIS_dp(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i, value in enumerate(nums):
            for j in range(i):
                if nums[j] < value:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp, default=0)


if __name__ == "__main__":
    solution = Solution()
    for nums, expected in [([4, 2, 3, 1, 5, 6], 4), ([3, 3, 3], 1), ([5, 4, 3], 1), ([], 0)]:
        assert solution.lengthOfLIS(nums) == expected
        assert solution.lengthOfLIS_dp(nums) == expected
    print("300. 最长递增子序列：通过")
