class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        res = 0
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                if leftMax - height[l] > 0:
                    res += leftMax - height[l]
                
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                if rightMax - height[r] > 0:
                    res += rightMax - height[r]
        return res