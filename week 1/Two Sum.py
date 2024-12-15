from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encountered = defaultdict(int)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in encountered:
                return i, encountered[diff]
            encountered[num] = i