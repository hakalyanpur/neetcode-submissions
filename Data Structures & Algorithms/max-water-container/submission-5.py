class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            # shorter side limits the water height
            if heights[l] < heights[r]:
                # left is shorter — it determines height
                area = heights[l] * (r - l)
                l += 1  # move left inward, hoping for taller bar
            else:
                # right is shorter (or equal) — it determines height
                area = heights[r] * (r - l)
                r -= 1  # move right inward, hoping for taller bar

            max_area = max(area, max_area)

        return max_area