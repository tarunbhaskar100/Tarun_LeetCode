class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        # push -1 to the stack
        stack.append(-1)
        # variable to store the max length
        max_len = 0
        # iterate over the string
        for i in range(len(s)):
            # if the current character is '('
            if s[i] == '(':
                # push the index to the stack
                stack.append(i)
            # if the current character is ')'
            else:
                # pop the top element from the stack
                stack.pop()
                # if the stack is not empty
                if len(stack) != 0:
                    # update the max length
                    max_len = max(max_len, i - stack[-1])
                # if the stack is empty
                else:
                    # push the index to the stack
                    stack.append(i)
        return max_len