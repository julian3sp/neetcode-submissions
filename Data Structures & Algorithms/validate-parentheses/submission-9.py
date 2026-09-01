class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        
        for l in s:
            if l in map.keys():
                stack.append(l)
            else:
                if not stack or l != map.get(stack[-1]): 
                    return False
                cur = stack.pop()

        return not stack