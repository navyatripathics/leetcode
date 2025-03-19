class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in d.keys():
                stack.append(i)
            elif i in d.values():
                if not stack or d[stack.pop()]!=i:
                    return False
        return len(stack)==0
