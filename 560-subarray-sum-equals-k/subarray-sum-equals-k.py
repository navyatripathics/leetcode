class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefixsum=0
        prefix_map=defaultdict(int)
        prefix_map[0]=1
        for num in nums:
            prefixsum+=num
            if prefixsum-k in prefix_map:
                count+=prefix_map[prefixsum-k]
            prefix_map[prefixsum]+=1
        return count