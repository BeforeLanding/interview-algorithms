"""200. 岛屿数量
题目：https://leetcode.cn/problems/number-of-islands/
题意：网格中 '1' 是陆地、'0' 是水，统计上下左右相连的陆地块数。

思路：扫描网格，每遇到未访问陆地，就发现一座新岛，答案加一。
从该格出发 DFS，把整座岛标记为 '2'，以后不会重复计数。
沿用灵茶山艾府的访问标记思路，用显式栈替代递归，避免 Python 递归过深。
时间 O(mn)，最坏额外空间 O(mn)。会修改 grid；保留原网格可传 [row[:] for row in grid]。
易错：入栈时立即标记，避免同一格被重复入栈；对角相邻不算连接。

参考：灵茶山艾府，网格 DFS。
https://leetcode.cn/problems/number-of-islands/solutions/2965773/ba-fang-wen-guo-de-ge-zi-cha-shang-qi-zi-9gs0/
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                ans += 1
                grid[i][j] = "2"
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            grid[nx][ny] = "2"
                            stack.append((nx, ny))
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.numIslands([list("1100"), list("0101"), list("0001")]) == 2
    assert solution.numIslands([list("10"), list("01")]) == 2
    assert solution.numIslands([["0"]]) == 0
    assert solution.numIslands([["1"] * 300 for _ in range(300)]) == 1
    assert solution.numIslands([]) == 0
    print("200. 岛屿数量：通过")
