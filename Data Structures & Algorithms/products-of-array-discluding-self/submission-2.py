class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_arr = [1] * n
        r_arr = [1] * n
        l_mult = 1
        r_mult = 1

        # Pass 1: left products (left → right)
        for i in range(n):
            l_arr[i] = l_mult
            l_mult *= nums[i] 

        # Pass 2: right products (right → left)
        for i in range(n-1, -1, -1):
            r_arr[i] = r_mult
            r_mult *= nums[i]

        # Pass 3: combine
        #return [i * j for i, j in zip(l_arr, r_arr)]

        result = []
        for i in range(n):
            result.append(l_arr[i] * r_arr[i])
        
        return result
        