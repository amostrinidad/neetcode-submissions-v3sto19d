class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for parentheses in s:
            if parentheses in matches.values():
                stack.append(parentheses)
            elif parentheses in matches:
                if not stack or stack.pop() != matches[parentheses]:
                    return False
            
        return len(stack) == 0