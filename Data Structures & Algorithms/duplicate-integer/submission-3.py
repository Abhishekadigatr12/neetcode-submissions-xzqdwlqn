class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]==nums[j]:
                   return True
        return False
        