class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board :
            return 0
        n=len(board)
        m=len(board[0])
        q=deque()
        direction=[(-1,0),(0,-1),(1,0),(0,1)]
        #marking all the O in boundary as T
        for i in range(n):
            for j in [0, m - 1]:  # First and last column
                if board[i][j] == 'O':
                    q.append((i, j))
                    board[i][j] = 'T'
        
        for j in range(m):
            for i in [0, n - 1]:  # First and last row
                if board[i][j] == 'O':
                    q.append((i, j))
                    board[i][j] = 'T'
        while q:
            row,col=q.popleft()
            for dr,dc in direction:
                new_r,new_c=row+dr,col+dc
                if 0<=new_r<n and 0<=new_c<m and board[new_r][new_c]=='O':
                    board[new_r][new_c]='T'
                    q.append((new_r,new_c))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Convert captured region
                elif board[i][j] == 'T':
                    board[i][j] = 'O'  # Restore non-captured region