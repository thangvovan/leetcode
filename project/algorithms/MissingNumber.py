class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        leng = len(nums)

        sum = 0
        for num in nums:
            sum += num
        
        return int((leng * (leng+1)) / 2) - sum