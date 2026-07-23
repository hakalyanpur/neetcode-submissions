class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        numSet = set(nums)

        for n in numSet:
            if (n - 1) not in numSet:
                # potential start of sequence
                current_streak = 0
                while (n + current_streak) in numSet:
                    current_streak += 1
                
                longest_streak = max (longest_streak,current_streak )
        
        return longest_streak
