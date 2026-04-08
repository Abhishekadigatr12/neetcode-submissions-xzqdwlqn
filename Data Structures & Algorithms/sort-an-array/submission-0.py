class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0,n):
            for j in range(n-i-1):
                if nums[j+1]< nums[j]:
                    nums[j+1],nums[j] = nums[j],nums[j+1]
        return nums