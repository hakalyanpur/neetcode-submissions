class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        c = Counter(nums)
        
        for num,count in c.most_common(k):
            res.append(num)
        
        return res