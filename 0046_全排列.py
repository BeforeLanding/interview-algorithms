"""46. 全排列
题目：https://leetcode.cn/problems/permutations/
题意：给定没有重复元素的数组，返回所有排列。

思路：从左到右填位置，每次选择一个还没用过的数。
used 标记哪些下标已选，path 保存当前排列；填满后复制进答案。
一次选择结束后撤销标记，让下一条分支可以重新选择该数。
时间 O(n * n!)；不计输出，额外空间 O(n)，输出空间 O(n * n!)。不修改输入。
易错：存答案时必须复制 path；本题不包含重复元素，含重复元素请看第 47 题。

参考：灵茶山艾府，排列型回溯。
https://leetcode.cn/problems/permutations/solutions/2079585/hui-su-bu-hui-xie-tao-lu-zai-ci-jing-que-6hrh/
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = [0] * n
        used = [False] * n

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            for j, value in enumerate(nums):
                if not used[j]:
                    path[i] = value
                    used[j] = True
                    dfs(i + 1)
                    used[j] = False  # 恢复现场；path[i] 会被下一次选择覆盖

        dfs(0)
        return ans


if __name__ == "__main__":
    from itertools import permutations

    solution = Solution()
    nums = [2, 4, 6]
    assert sorted(solution.permute(nums)) == sorted(map(list, permutations(nums)))
    assert nums == [2, 4, 6]
    assert solution.permute([8]) == [[8]]
    print("46. 全排列：通过")
