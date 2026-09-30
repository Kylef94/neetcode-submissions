from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        stack = deque()
        for char in s:
            if char in ["{","(", "["]:
                stack.append(char)
            else:
                if not stack or char != pairs[stack.pop()]:
                    return False
        
        if stack: return False
        return True
        