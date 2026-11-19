"""128. 最长连续序列
题目：https://leetcode.cn/problems/longest-consecutive-sequence/
题意：找出数值连续的最长序列长度，不要求在原数组中位置连续。

思路：先将数字放入集合。只从没有前驱 x-1 的数字 x 开始，向后查找连续数字。
关键优化：遍历集合而非原数组，去掉重复值；只从每段序列的起点开始，避免重复扫描。

时间复杂度：O(n)，其中 n 是 nums 的长度。在二重循环中，每个元素至多遍历两次：在外层循环中遍历一次，在内层循环中遍历一次。
所以二重循环的时间复杂度是 O(n) 的。比如 nums=[1,2,3,4]，其中 2,3,4 不会进入内层循环，只有 1 会进入内层循环。
空间复杂度：O(m)。其中 m 是 nums 中的不同元素个数。
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)  # 把 nums 转成哈希集合
        m = len(st)

        ans = 0
        for x in st:  # 遍历哈希集合
            if x - 1 in st:  # 如果 x 不是序列的起点，直接跳过
                continue
            # x 是序列的起点
            y = x + 1
            while y in st:  # 不断查找下一个数是否在哈希集合中
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ans = max(ans, y - x)  # 从 x 到 y-1 一共 y-x 个数
            if ans * 2 >= m:  # ans 不可能变得更大
                break
        return ans
