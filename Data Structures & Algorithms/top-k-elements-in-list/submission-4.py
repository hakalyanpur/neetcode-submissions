class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # c = Counter(nums)
        # for num,count in c.most_common(k):
        #     res.append(num)        
        # return res

        c = Counter(nums)
        heap = []
        res = []

        for num, count in c.items():
            heapq.heappush(heap, (-count, num))  # negate for max-heap

        for i in range(k):
            count, num = heapq.heappop(heap)  # pops most frequent first
            res.append(num)

        return res
        
        

