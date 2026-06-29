class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0:
                return 0
            left = 0
            summ = 0
            count = 0
            for right in range(len(nums)):
                if nums[right] == 1:
                    summ += 1
                while summ > goal:
                    if nums[left] == 1:
                        summ -= 1
                    left += 1
                count += (right - left + 1)
            return count
        return atMost(goal) - atMost(goal - 1)