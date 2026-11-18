"""46. 全排列
题目：https://leetcode.cn/problems/permutations/
题意：给定没有重复元素的数组，返回所有排列。

思路：从左到右填位置，每次选择一个还没用过的数。
used 标记哪些下标已选，path 保存当前排列；填满后复制进答案。
一次选择结束后撤销标记，让下一条分支可以重新选择该数。

时间复杂度：O(n⋅n!)，其中 n 为 nums 的长度。视频中提到，搜索树中的节点个数低于 3⋅n!。实际上，精确值为 ⌊e⋅n!⌋，其中 e=2.718⋯ 为自然常数。
有 O(n!) 个叶节点，每个叶节点花费 O(n) 的时间复制 path 数组，因此时间复杂度为 O(n⋅n!)。
空间复杂度：O(n)。返回值的空间不计入。
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n  # 所有排列的长度都是一样的 n
        on_path = [False] * n
        ans = []

        # 枚举 path[i] 填 nums 的哪个数
        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())  # 也可以写 path[:]
                return
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]  # 从没有选的数字中选一个
                    on_path[j] = True  # 已选上
                    dfs(i + 1)
                    on_path[j] = False  # 恢复现场
                    # 注意 path 无需恢复现场，因为排列长度固定，直接覆盖就行

        dfs(0)
        return ans
