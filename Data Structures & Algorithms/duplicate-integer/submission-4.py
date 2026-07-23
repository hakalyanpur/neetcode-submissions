class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Solution 1
        #return len(set(nums)) < len (nums)

        # Solution 2
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False