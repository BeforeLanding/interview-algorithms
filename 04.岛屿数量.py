"""200. 岛屿数量
题目：https://leetcode.cn/problems/number-of-islands/
题意：网格中 '1' 是陆地、'0' 是水，统计上下左右相连的陆地块数。

思路：遍历数组，找到'1'也就是陆地，先将岛屿数量+1，然后从该点开始dfs，每一步都可以上下左右移动，确保将整座岛（连通的陆地部分内容）全部更新为'2'，下次遍历时不会重复访问。

时间复杂度：O(mn)，其中 m 和 n 分别是 grid 的行数和列数。
由于 DFS 中修改了 grid[i][j] = '2'，当我们访问一个访问过的格子时，会触发 if grid[i][j] != '1': return。
只有首次访问一个格子时，才会继续递归，其余情况不会继续递归。每次插上一个旗子只需要 O(1) 的时间，插上至多 mn 个旗子，就需要 O(mn) 的时间。
空间复杂度：O(mn)。最坏情况下，对于蛇形陆地、蚊香型陆地等，递归需要 O(mn) 的栈空间。

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(i:int,j:int) -> None:
            if (
                i < 0 or i >= n
                or j < 0 or j >= m
                or grid[i][j] != '1'
            ):
                return
            
            grid[i][j] = 2
            dfs(i, j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

        ans = 0
        for i,row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '1':
                    dfs(i,j)
                    ans += 1
        return ans
