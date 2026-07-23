class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_ptr = 0
        count = 0
        dup_set = set()

        for right_ptr in range(len(s)):
            # dup detected
            while s[right_ptr] in dup_set:
                dup_set.remove(s[left_ptr])
                left_ptr += 1


            dup_set.add(s[right_ptr])
            curr_window_size = right_ptr - left_ptr + 1
            count = max(count,curr_window_size)
        
        return count