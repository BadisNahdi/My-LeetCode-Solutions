class Solution(object):
    def partition(self, s):
        res = []
        subres = []
        def isPalindrome(a):
            return a == a[::-1]
        def dfs(i):
            if i >= len(s):
                res.append(subres[:])
            for j in range(i,len(s)):
                if (isPalindrome(s[i:j+1])):
                    subres.append(s[i:j+1])
                    dfs(j+1)
                    subres.pop()
        dfs(0)
        return(res)