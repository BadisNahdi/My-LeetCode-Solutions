class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        l, r = 1, n
        while(l<=r):
            m = (l+r)//2
            
            if(((m)*(m+1)//2)>n):
                r = m - 1
            else:
                l = m + 1
                res = max(m, res)
            
        return res