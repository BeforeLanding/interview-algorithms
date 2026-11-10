"""15. 三数之和
题目：https://leetcode.cn/problems/3sum/
题意：找出和为 0 的所有不重复三元组，三个元素的下标必须不同。

思路：排序后固定第一个数，在右侧用相向双指针寻找另外两个数。
和偏小就增大左指针，和偏大就减小右指针。固定值和命中后的值都需要去重。
两个剪枝：当前数加后面最小两数仍大于 0，可以结束；加最大两数仍小于 0，跳过当前数。
时间 O(n²)；不计输出，Python 排序最坏额外空间 O(n)。会原地排序 nums。
易错：去掉重复的三元组，不是先把输入数组去重；[0,0,0] 是合法答案。

参考：灵茶山艾府，双指针与两个剪枝优化；此处重新整理讲解和示例。
https://leetcode.cn/problems/3sum/solutions/1968332/shuang-zhi-zhen-xiang-bu-ming-bai-yi-ge-pno55/
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            value = nums[i]
            if i > 0 and value == nums[i - 1]:
                continue
            if value + nums[i + 1] + nums[i + 2] > 0:
                break
            if value + nums[-2] + nums[-1] < 0:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = value + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.threeSum([-3, -1, 0, 1, 2, 3]) == [[-3, 0, 3], [-3, 1, 2], [-1, 0, 1]]
    assert solution.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert solution.threeSum([1, 2, 3]) == []
    assert solution.threeSum([]) == []
    print("15. 三数之和：通过")
