class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n=len(players)
        m=len(trainers)
        left=0
        right=0
        while (left<n and right<m):
            if players[left]<=trainers[right]:
                left+=1
                right+=1
            else:
                right+=1
        return left