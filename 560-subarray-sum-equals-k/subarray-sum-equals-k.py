from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix_map=defaultdict(int)
        prefix_map[0]=1
        curr_sum=0
        for num in nums:
            curr_sum+=num
            if (curr_sum-k) in prefix_map:
                count+=prefix_map[curr_sum-k]
            prefix_map[curr_sum]+=1
        return count 