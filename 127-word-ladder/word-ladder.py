class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        w=set(wordList)
        q=deque([(beginWord,1)])
        visited=set()
        visited.add(beginWord)
        while q:
            node,level=q.popleft()
            if node==endWord:
                return level
            for i in range(len(node)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newword=node[:i]+c+node[i+1:]
                    if newword in w and newword not in visited:
                        visited.add(newword)
                        q.append((newword,level+1))
        return 0