class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
                return 1
            res=power(x,n//2) 
            return x*res*res if n%2==1 else res*res 
        if n>0:
            return power(x,n)
        else:
            return power(1/x,abs(n))