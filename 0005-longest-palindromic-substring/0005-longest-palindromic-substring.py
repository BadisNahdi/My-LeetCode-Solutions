class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = ""
        length = 0
        for i in range(len(s)):
            n = i
            p = i
            while n < len(s) and p > -1 and s[n] == s[p]:
                if (n - p + 1 ) > length:
                    ls = s[p:n+1]
                    length = n - p +1
                n += 1
                p -= 1
            
            p = i
            n = i + 1
            while n < len(s) and p > -1 and s[n] == s[p]:
                if (n - p +1) > length:
                    ls = s[p:n+1]
                    length = n - p +1
                n += 1
                p -= 1
        
        return ls
