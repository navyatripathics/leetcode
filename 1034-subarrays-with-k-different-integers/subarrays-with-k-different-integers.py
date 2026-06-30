class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            left=0
            count=0
            hash={}
            for right in range(len(nums)):
                if nums[right] not in hash:
                    hash[nums[right]]=1
                else:
                    hash[nums[right]]+=1
                while len(hash)>k:
                    if nums[left] in hash:
                        hash[nums[left]]-=1
                    if hash[nums[left]]==0:
                        del hash[nums[left]]
                    left+=1
                count+=right-left+1
            return count
        return atmost(k)-atmost(k-1)