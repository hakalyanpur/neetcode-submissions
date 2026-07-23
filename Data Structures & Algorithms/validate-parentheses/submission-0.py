class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        """
        stack.append("a")   # push
        stack.append("b")
        stack.pop()          # pop → "b" (last in, first out)
        stack[-1]            # peek at top without removing
        len(stack) == 0      # check if empty
        """
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char == "[" or char == "{" or char == "(":
                stack.append(char)
            else:
                if len(stack) == 0 or close_to_open[char] != stack.pop():
                    return False

        return len(stack) == 0