class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        l = 0
        for i in s:
            if not(i-1 in s):
                curr = i
                c = 1
                while curr+1 in s:
                    c+=1
                    curr+=1
                l = max(l, c)
        return l