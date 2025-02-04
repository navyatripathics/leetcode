class Solution(object):
    def maxAscendingSum(self, nums):
        max_sum = 0  # Store the maximum sum
        n = len(nums)

        for i in range(n):  # Start of subarray
            curr_sum = nums[i]  # Initialize sum with first element
            for j in range(i + 1, n):  # Expand subarray
                if nums[j] > nums[j - 1]:  # Maintain ascending order
                    curr_sum += nums[j]
                else:
                    break  # Stop if order breaks
            max_sum = max(max_sum, curr_sum)  # Update max sum
        
        return max_sum
