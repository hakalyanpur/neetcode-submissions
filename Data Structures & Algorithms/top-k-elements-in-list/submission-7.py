class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        # build a freqmap
        c = Counter(nums)

        # iterate over map to build the heap
        for num, count in c.items():
            heapq.heappush(heap,(-count, num))
        
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res


