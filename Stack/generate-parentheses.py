# https://leetcode.com/problems/generate-parentheses/description/


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open, close):
            # base case
            if open == close == n:
                res.append("".join(stack))
                return

            # recursive case
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return res


s = Solution()


print(
    "Example 1: ", s.generateParenthesis(3)
)  # ["((()))","(()())","(())()","()(())","()()()"]

print("Example 2: ", s.generateParenthesis(1))  # ["()"]
