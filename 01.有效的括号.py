"""20. 有效的括号
题目：https://leetcode.cn/problems/valid-parentheses/
题意：字符串只含 ()[]{}，判断括号能否按正确的类型和嵌套顺序匹配。

思路：左括号入栈；遇到右括号时，必须与栈顶左括号匹配。
若栈为空或类型不匹配，立即返回 False；遍历后还需检查栈是否为空。
时间 O(n)，最坏空间 O(n)。不修改输入。
易错：只统计左右括号数量不够，例如 ([)] 数量相等但顺序错误。

来源说明：本题采用通用栈解法，未核实到可直接引用的灵茶山艾府原文，
因此不将此实现署为其题解。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or stack.pop() != pairs[char]:
                return False
        return not stack


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("{[()]}()")
    assert not solution.isValid("([)]")
    assert not solution.isValid("]]")
    assert not solution.isValid("((")
    assert not solution.isValid("(")
    assert solution.isValid("")
    print("20. 有效的括号：通过")
