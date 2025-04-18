class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)
        if endWord not in wordSet:
            return 0
        q=deque([(beginWord,1)])
        visited=set()
        visited.add(beginWord)
        while q:
            word,step=q.popleft()
            for i in range(len(word)):
                for j in string.ascii_lowercase:
                    newword=word[:i]+j+word[i+1:]
                    
                    if newword==endWord:
                            return step+1
                    if newword in wordSet and newword not in visited:
                        q.append((newword,step+1))
                        visited.add(newword)
        return 0