class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)

        for citation in citations:
            bucket[min(citation, n)] += 1

        count = 0
        for h in range(n, -1, -1):
            count += bucket[h]
            if h <= count:
                return h  

    def hIndex2(self, citations: list[int]) -> int:
        n = len(citations)
        left, right = 0, n

        while left < right:
            mid = left + (right - left) // 2
            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid + 1
        return n - left