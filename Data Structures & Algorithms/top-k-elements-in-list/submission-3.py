class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # c = Counter(nums)
        # for num,count in c.most_common(k):
        #     res.append(num)        
        # return res

        c = Counter(nums)           # {1: 3, 2: 2, 3: 1}
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in c.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

