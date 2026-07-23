class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0 or close_to_open[char] != stack.pop():
                    return False

        return len(stack) == 0