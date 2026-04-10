class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for parenthesis in s:
            if parenthesis in matches.values():
                stack.append(parenthesis)
            elif parenthesis in matches:
                if not stack or stack.pop() != matches[parenthesis]:
                    return False

        return len(stack) == 0
            
        
            
            
