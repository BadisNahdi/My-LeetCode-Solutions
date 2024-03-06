class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (word == s[i:i+len(word)] and i+len(word)<=len(s)):
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        return(dp[0])