class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashmap={}
        count=0
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
            if i - k in hashmap:
                count += hashmap[i - k]
            if i + k in hashmap:
                count += hashmap[i + k]
        return count