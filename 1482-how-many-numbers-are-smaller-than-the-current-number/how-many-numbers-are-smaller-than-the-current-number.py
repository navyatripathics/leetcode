class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):  # Loop through each element
            count = 0
            for j in range(len(nums)):  # Compare with every other element
                if nums[j] < nums[i]:  # Count numbers smaller than nums[i]
                    count += 1
            result.append(count)  # Store the count in result list
        return result
        