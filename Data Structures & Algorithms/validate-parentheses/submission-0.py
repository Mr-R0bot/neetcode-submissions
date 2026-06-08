class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracks = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in bracks:
                if len(stack)==0 or stack[-1]!=bracks[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return False if len(stack) > 0 else True
            
            