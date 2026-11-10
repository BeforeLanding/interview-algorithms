"""42. 接雨水
题目：https://leetcode.cn/problems/trapping-rain-water/
题意：柱子宽度均为 1，计算下雨后能存多少水。

思路：每格水量是 min(左侧最高柱, 右侧最高柱) - 当前高度。
从两端向中间扫描，维护已扫描的左右最高柱。
若左侧最高柱更低，右边已经有足够高的柱子，左侧水量就确定了；反之处理右侧。
时间 O(n)，额外空间 O(1)。不修改输入。

参考：灵茶山艾府，相向双指针思路；此处重新整理注释和示例。
https://leetcode.cn/problems/trapping-rain-water/solutions/1974340/zuo-liao-nbian-huan-bu-hui-yi-ge-shi-pin-ukwm/
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = ans = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.trap([4, 1, 3, 1, 5]) == 7
    assert solution.trap([2, 0, 2]) == 2
    assert solution.trap([1, 2, 3]) == 0
    assert solution.trap([]) == 0
    print("42. 接雨水：通过")
