class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)]for _ in range(n)]
        def f(ind, target):
            if ind==0:
                if target%coins[0]==0:
                    return target//coins[0]
                return float('inf')
            if dp[ind][target]!=-1:
                return dp[ind][target]
            not_take=0+f(ind-1,target)
            take = float('inf')
            if coins[ind]<=target:
                take=1+f(ind,target-coins[ind])
            dp[ind][target]=min(take,not_take)
            return dp[ind][target]
        ans = f(n - 1, amount)
        return -1 if ans == float('inf') else ans