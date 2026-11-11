class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for o in s:
            if o == "]":
                if not stack or stack[-1]!="[":
                    return False
                stack.pop()
            elif o == "}":
                if not stack or stack[-1]!="{":
                    return False
                stack.pop()
            elif o == ")":
                if not stack or stack[-1]!="(":
                    return False
                stack.pop()
            else:
                stack.append(o)
        return True if not stack else False