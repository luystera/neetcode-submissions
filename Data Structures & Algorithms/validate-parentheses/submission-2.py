class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            # append if left bracket
            if c in pairs.values():
                stack.append(c)
            # must be right bracket, check if it matches
            else:
                if not stack or stack.pop() != pairs[c]:
                    return False
        
        if (stack):
            return False
        return True

