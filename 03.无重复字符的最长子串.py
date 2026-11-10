"""3. 无重复字符的最长子串
题目：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
题意：求没有重复字符的最长连续子串的长度。

思路：右端点逐个加入字符，用计数表维护窗口。
新字符重复时，不断移走左端字符，直到窗口重新合法，再更新长度。
两个指针各自最多走 n 步，所以嵌套循环整体仍是 O(n)。
时间 O(n)，空间 O(min(n, 字符集大小))。不修改输入。
易错：子串必须连续；缩小窗口用 while，不能只用 if。

参考：灵茶山艾府，滑动窗口计数写法；此处重新整理讲解和示例。
https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/1959540/xia-biao-zong-suan-cuo-qing-kan-zhe-by-e-iaks/
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = ans = 0
        for right, char in enumerate(s):
            count[char] += 1
            while count[char] > 1:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcaef") == 5
    assert solution.lengthOfLongestSubstring("abba") == 2
    assert solution.lengthOfLongestSubstring("aaaa") == 1
    assert solution.lengthOfLongestSubstring("") == 0
    print("3. 无重复字符的最长子串：通过")
