class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices={}
        for i,num in enumerate(nums):
            counter=target-num
            if counter in nums_indices:
                return [nums_indices[counter],i]
            nums_indices[num]=i
        return []