class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                Tsum = nums[i]+nums[l]+nums[r]
                if Tsum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif Tsum < 0:
                    l+=1
                else:
                    r-=1
        return res