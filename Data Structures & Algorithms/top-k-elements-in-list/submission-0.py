import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
    
    # Step 2: Build a max-heap using negative frequencies
        heap = [(-count, num) for num, count in freq_map.items()]
        heapq.heapify(heap)
    
    # Step 3: Extract k most frequent elements
        result = []
        for _ in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)
    
        return result
