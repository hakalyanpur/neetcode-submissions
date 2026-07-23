class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        
        # build a freqmap
        c = Counter(nums)

        # iterate over map to build the heap
        for num, count in c.items():
            heapq.heappush(heap, (count, num)) # min heap

            if len(heap) > k:
                heapq.heappop(heap) # evict smallest
        

        return [num for count, num in heap]


