class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        last = nums[len(nums)-1]
        beforelast = nums[len(nums)-2]
        dp = { length-1: nums[length-1], length-2: nums[length-2]}
        def bfs(i):
            if i == length:
                return 0
            if dp.has_key(i):
                return dp[i]
            one = nums[i]+bfs(i+2)
            two = nums[i]+bfs(i+3)
            if one > two:
                dp[i] = one
            else:
                dp[i] = two
            return dp[i]
            
        
        if (bfs(0)>bfs(1)):
            return bfs(0)
        return bfs(1)
                
        