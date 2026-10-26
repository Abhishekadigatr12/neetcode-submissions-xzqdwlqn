class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Prune 1: Smallest possible 4 elements are already too large
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # Prune 2: Largest possible 4 elements with nums[i] are still too small
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Prune 3: Smallest remaining 3 elements are too large
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # Prune 4: Largest remaining 3 elements are too small
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1

        return res       