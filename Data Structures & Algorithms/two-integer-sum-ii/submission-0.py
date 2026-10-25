class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            curTar = numbers[l]+numbers[r]
            if curTar == target:
                return [l+1,r+1]
            elif curTar < target:
                l+=1
            else:
                r-=1
        return []
