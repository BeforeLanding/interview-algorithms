"""300. 最长递增子序列
题目：https://leetcode.cn/problems/longest-increasing-subsequence/
题意：可以删除元素但不能改变顺序，求严格递增的最长子序列长度。

思路： 记忆化搜索/递推/二分查找
方法一：记忆化搜索
dfs(i) 表示以 nums[i] 结尾的最长递增子序列（LIS）的长度。
枚举子序列的倒数第二个数的下标是 j，如果 nums[j]<nums[i]，那么有dfs(i)=dfs(j)+1取最大值。
注意 nums[i] 可以单独形成一个长为 1 的子序列。
时间 O(n log n)，空间 O(n)。两个解法都不修改输入。

方法二：递推
同记忆化搜索，f[i] 表示以 nums[i] 结尾的最长递增子序列（LIS）的长度。

方法三：贪心 + 二分查找
假设 f[3] 和 f[4] 的值都等于 2，且 nums[3]=99999，nums[4]=9。
我们现在要计算 f[5]。想一想，谁更容易满足上面代码中的 if (nums[j] < nums[i])？这里 i=5，j=3 或者 4。
nums[4] 更小，更容易满足 if (nums[j] < nums[i])。更大的 nums[3] 虽然也可能满足条件，但由于 f[3]=f[4]，在更新 f[5] 时，二者的效果是一样的，所以 nums[3] 是个无用数据。
换句话说，对于相同的 f 值，我们只需保留更小的 nums[i]。
注：这个「去掉无用数据」的想法和单调栈是一样的。
因此，定义 g[i] 表示 f[j]=i+1 时，nums[j] 的最小值。也就是长为 i+1 的上升子序列的末尾元素的最小值。这里 +1 是因为 f[j] 至少是 1，g[0] 对应的不是 f[j]=0，而是 f[j]=1。
"""
# 方法一
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1  # 加一提到循环外面

        return max(dfs(i) for i in range(len(nums)))
# 时间复杂度：O(n2)，其中 n 为 nums 的长度。由于每个状态只会计算一次，动态规划的时间复杂度 = 状态个数 × 单个状态的计算时间。本题中状态个数等于 O(n)，单个状态的计算时间为 O(n)，
所以动态规划的时间复杂度为 O(n2)。
# 空间复杂度：O(n)。保存多少状态，就需要多少空间。

# 方法二
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                if x > y:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return max(f)
# 时间复杂度：O(n2)，其中 n 为 nums 的长度。
# 空间复杂度：O(n)。

# 方法三
# 写法1 额外空间
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            j = bisect_left(g, x)
            if j == len(g):  # >=x 的 g[j] 不存在
                g.append(x)
            else:
                g[j] = x
        return len(g)
# 时间复杂度：O(nlogn)，其中 n 为 nums 的长度。
# 空间复杂度：O(n)。

# 写法2 原地修改
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0  # g 的长度
        for x in nums:
            j = bisect_left(nums, x, 0, ng)
            nums[j] = x
            if j == ng:  # >=x 的 g[j] 不存在
                ng += 1 
        return ng
# 时间复杂度：O(nlogn)，其中 n 为 nums 的长度。
# 空间复杂度：O(1)。
