import heapq
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
			
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
			
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
					
					
        level, res = 0, 0
        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(height, level)

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
					
                    if heightMap[i][j] < level:
                        res += level - heightMap[i][j]
						
                    heightMap[i][j] = -1

        return res