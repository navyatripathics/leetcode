class Solution:
    def __init__(self):
        self.dp={}
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]