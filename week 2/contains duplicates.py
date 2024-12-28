class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        encountered = set()
        for n in nums:
            if n in encountered:
                return True
            encountered.add(n)
        return False