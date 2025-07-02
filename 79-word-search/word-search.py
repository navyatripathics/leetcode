class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        def dfs(ind,i,j):
            if ind==len(word):
                return True
            if i<0 or j<0 or j==col or i==row or board[i][j]!=word[ind]:
                return False
            x=board[i][j]
            board[i][j]='*'
            r=[0,1,0,-1]
            c=[1,0,-1,0]
            for d in range(4):
                if dfs(ind+1,i+r[d],j+c[d])==True:
                    return True
            board[i][j]=x
            return False
        for i in range(row):
            for j in range(col):
                if dfs(0,i,j)==True:
                    return True
        return False
