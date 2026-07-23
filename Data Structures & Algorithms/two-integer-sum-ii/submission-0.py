class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if target == curr_sum:
                return [left + 1, right + 1];

            if target > curr_sum:
                left += 1

            else:
                right -= 1

        

        return -1
