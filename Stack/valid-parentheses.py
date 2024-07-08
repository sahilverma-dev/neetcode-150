class Solution:
    def isValid(str):
        stack = []

        # define opening closing and pairing parentheses with their opening and closing parentheses
        opening = "({["
        closing = ")}]"
        pairs = {")": "(", "}": "{", "]": "["}

        for i in str:
            # push opening elements on the stack
            if i in opening:
                stack.append(i)
            # push opening elements on the stack
            elif i in closing:
                # check is stack is empty (there's no opening parentheses) OR last opening parentheses not match with current closing one
                if not stack or stack.pop() != pairs[i]:
                    return False

        # after removal of all paired parentheses if size of the stack is zero then its a valid parentheses
        return len(stack) == 0


s = Solution


print(s.isValid("([{}])"))  # True
print(s.isValid("[]"))  # True
print(s.isValid("[(])"))  # False
