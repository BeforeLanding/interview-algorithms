"""128. 最长连续序列
题目：https://leetcode.cn/problems/longest-consecutive-sequence/
题意：找出数值连续的最长序列长度，不要求在原数组中位置连续。

思路：先将数字放入集合。只从没有前驱 x-1 的数字 x 开始，向后查找连续数字。
关键优化：遍历集合而非原数组，去掉重复值；只从每段序列的起点开始，避免重复扫描。
每个不同数字只参与所属连续段的一次扩展，平均时间 O(n)，空间 O(n)。不修改输入。
易错：本题要求 O(n)，不能直接排序；它与“最长递增子序列”的顺序要求不同。

参考：灵茶山艾府，两个关键优化。
https://leetcode.cn/problems/longest-consecutive-sequence/solution/ha-xi-biao-on-zuo-fa-pythonjavacgojsrust-whop/
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        ans = 0
        for start in values:
            if start - 1 in values:
                continue
            end = start
            while end + 1 in values:
                end += 1
            ans = max(ans, end - start + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestConsecutive([8, 2, 5, 3, 4, 2]) == 4
    assert solution.longestConsecutive([-2, -1, 0, 2]) == 3
    assert solution.longestConsecutive([1, 1, 1]) == 1
    assert solution.longestConsecutive([]) == 0
    print("128. 最长连续序列：通过")
