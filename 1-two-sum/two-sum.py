class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in d:
                return [d[complement],i]
            d[num]=i