"""3. 无重复字符的最长子串
题目：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
题意：求没有重复字符的最长连续子串的长度。

思路：滑动窗口
右端点逐个加入字符，用计数表维护窗口。
新字符重复时，不断移走左端字符，直到窗口重新合法，再更新长度。
两个指针各自最多走 n 步，所以嵌套循环整体仍是 O(n)。
时间 O(n)，空间 O(min(n, 字符集大小))。不修改输入。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        n = len(s)
        cnt = Counter()
        for right,c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans
