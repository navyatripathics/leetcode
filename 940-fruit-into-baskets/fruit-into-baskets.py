class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap={}
        maxlen=0
        left=0
        for right in range(left,len(fruits)):
            if fruits[right] in hashmap:
                hashmap[fruits[right]]+=1
            else:
                hashmap[fruits[right]]=1
            while len(hashmap)>2:
                hashmap[fruits[left]]-=1
                if hashmap[fruits[left]]==0:
                    del hashmap[fruits[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen