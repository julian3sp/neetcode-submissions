class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = { ")":"(", "]":"[", "}":"{"}

        for c in s:
            if( c == "(" or c =="[" or c == "{"):
                stack.append(c)
                continue

            if(not stack or Map[c] != stack[-1]):
                return False
            else:
                stack.pop()
        return not stack 
