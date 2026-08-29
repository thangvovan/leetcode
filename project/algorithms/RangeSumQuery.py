from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = [0]
        sum = 0
        for num in nums:
            sum += num
            self.nums.append(sum)

    def update(self, index: int, val: int) -> None:
        v = val - self.nums[index+1] + self.nums[index]
        for i in range(index+1, len(self.nums)):
            self.nums[i] += v

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]