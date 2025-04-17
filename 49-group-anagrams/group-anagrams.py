class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in range(len(strs)):
            a= tuple(sorted(strs[i]))
            if a not in hashmap:
                hashmap[a]=[strs[i]]
            else:
                hashmap[a].append(strs[i])
        return list(hashmap.values())