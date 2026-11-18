"""20. 有效的括号
题目：https://leetcode.cn/problems/valid-parentheses/
题意：字符串只含 ()[]{}，判断括号能否按正确的类型和嵌套顺序匹配。

思路： "邻项消除"问题都可以用栈解决。
以 s={[()]} 为例：
创建一个空栈。
从左到右遍历 s。
s[0]={，这是一个左括号，入栈。
s[1]=[，这是一个左括号，入栈。
s[2]=(，这是一个左括号，入栈。
s[3]=)，这是一个右括号，它必须和栈顶的 ( 组成一对（消除），弹出栈顶。
s[4]=]，这是一个右括号，它必须和栈顶的 [ 组成一对（消除），弹出栈顶。
s[5]=}，这是一个右括号，它必须和栈顶的 { 组成一对（消除），弹出栈顶。
遍历结束，由于栈为空，说明所有括号均已匹配完毕，返回 true。反之，如果在遍历的过程中，发现栈为空，或者括号类型不匹配的情况，返回 false。此外，如果遍历结束栈不为空，说明还有没匹配的左括号，返回 false。

时间 O(n)，最坏空间 O(n)。不修改输入。
易错：只统计左右括号数量不够，例如 ([)] 数量相等但顺序错误。
"""

# 写法1:
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:  # s 长度必须是偶数
            return False
        mp = {')': '(', ']': '[', '}': '{'}
        st = []
        for c in s:
            if c not in mp:  # c 是左括号
                st.append(c)  # 入栈
            elif not st or st.pop() != mp[c]:  # c 是右括号
                return False  # 没有左括号，或者左括号类型不对
        return not st  # 所有左括号必须匹配完毕

# 写法2:
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:  # s 长度必须是偶数
            return False
        st = []
        for c in s:
            if c == '(':
                st.append(')')  # 入栈对应的右括号
            elif c == '[':
                st.append(']')
            elif c == '{':
                st.append('}')
            elif not st or st.pop() != c:  # c 是右括号
                return False  # 没有左括号，或者左括号类型不对
        return not st  # 所有左括号必须匹配完毕
