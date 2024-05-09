class Solution(object):
    def permute(self, nums):
        ret = []
        sol = []
        n = len(nums)
        def dfs():
            if len(sol) == n:
                ret.append(sol[:])
                return
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    dfs()
                    sol.pop()
        dfs()
        return ret