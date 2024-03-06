class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount+1)
        dp[0] = 1
        while(coins):
            coin = coins.pop(0)
            for i in range(amount+1):
                if dp[i]:
                    num = coin+i
                    if(num<amount+1):
                        dp[num]+=dp[i]
                    else:
                        break
        return(dp[amount])