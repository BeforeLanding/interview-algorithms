"""42. 接雨水
题目：https://leetcode.cn/problems/trapping-rain-water/
题意：柱子宽度均为 1，计算下雨后能存多少水。

思路：经典中的经典 前后缀分解/双指针/单调栈 三种解法都要会
"""

# 方法1：前后缀分解
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n  # pre_max[i] 表示从 height[0] 到 height[i] 的最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n  # suf_max[i] 表示从 height[i] 到 height[n-1] 的最大值
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h  # 累加每个水桶能接多少水
        return ans
# 时间复杂度：O(n)，其中 n 是 height 的长度。
# 空间复杂度：O(n)。

# 方法2：双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])  # 前缀最大值
            suf_max = max(suf_max, height[right])  # 后缀最大值
            if pre_max < suf_max:  # 可以确定 left 处的接水量
                ans += pre_max - height[left]
                left += 1  # 搞定了 left，现在问题缩小到 [left+1, right]
            else:  # 可以确定 right 处的接水量
                ans += suf_max - height[right]
                right -= 1  # 搞定了 right，现在问题缩小到 [left, right-1]
        return ans
# 时间复杂度：O(n)，其中 n 是 height 的长度。
# 空间复杂度：O(1)。

# 方法3：单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and height[st[-1]] <= h:
                bottom_h = height[st.pop()]
                if not st:  # 栈是空的
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h  # 面积的高
                ans += dh * (i - left - 1)
            st.append(i)
        return ans
# 时间复杂度：O(n)，其中 n 是 height 的长度。虽然我们写了个二重循环，但站在每个元素的视角看，这个元素在二重循环中最多入栈出栈各一次，因此循环次数之和是 O(n)，所以时间复杂度是 O(n)。
# 空间复杂度：O(min(n,U))，其中 U=max(height)−min(height)+1。注意栈中没有重复元素，在 height 值域很小的情况下，空间复杂度主要取决于 height 的值域范围。
