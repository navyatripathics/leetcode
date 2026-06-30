class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            left=0
            count=0
            odd_num=0
            for right in range(len(nums)):
                if nums[right]%2!=0:
                    odd_num+=1
                while odd_num>k:
                    if nums[left]%2!=0:
                        odd_num-=1
                    left+=1
                count+=right-left+1
            return count
        return atmost(k)-atmost(k-1)