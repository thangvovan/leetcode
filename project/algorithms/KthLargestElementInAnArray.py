import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for i in nums:
            heapq.heappush(maxheap, -i)
        for _ in range(k-1):
            heapq.heappop(maxheap)
        return -maxheap[0]