class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num] = 1
        result = []
        threshold = len(nums) // 3
        for num in d:
            if d[num] > threshold:
                result.append(num)
        return result
        