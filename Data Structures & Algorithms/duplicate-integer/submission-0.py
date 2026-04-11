class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = dict()
        for i,n in enumerate(nums):
            if n in r:
                return True
            r[n] = i
        return False