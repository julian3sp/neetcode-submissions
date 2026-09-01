class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        
        for l in s:
            if l in map.keys():
                stack.append(l)
            else:
                if not stack: 
                    return False
                cur = stack.pop()
                if l != map.get(cur):
                    return False
        if stack:
            return False
        return True