class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        max_area = 0

        while l <= r:
            if heights[l] < heights[r]:
                area = min(heights[l], heights[r]) * (r - l)
                l += 1
            else:
                area = min(heights[l], heights[r]) * (r - l)
                r -= 1                      
            
            max_area = max(area, max_area)
    

        return max_area