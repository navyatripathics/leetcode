class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate fixed number

            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # skip duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res
