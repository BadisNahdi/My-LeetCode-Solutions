class Solution(object):
    def letterCombinations(self, digits):
        res = []
        characters = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(i, s):
            if i == len(digits):
                res.append(s)
                return
            for c in characters[digits[i]]:
                backtrack(i+1, s+c)
        if(digits):
            backtrack(0, "")
        return(res)
            
        