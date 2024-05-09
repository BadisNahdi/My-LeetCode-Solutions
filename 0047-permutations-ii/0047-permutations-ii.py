class Solution(object):
    def permuteUnique(self, nums):
        res = []
        sol = []
        used = []
        def dfs():
            if (len(sol) == len(nums)) and (sol[:] not in res):
                res.append(sol[:])
                return
            for i in range(len(nums)):
                if(i not in used):
                    sol.append(nums[i])
                    used.append(i)
                    dfs()
                    used.pop()
                    sol.pop()
                    
        dfs()
        return res
                    
        