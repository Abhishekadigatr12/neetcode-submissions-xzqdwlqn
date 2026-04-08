class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        r = maxcount = 0
        for num in nums:
            count[num] += 1
            if maxcount<count[num]:
                r = num
                maxcount = count[num]
        return r