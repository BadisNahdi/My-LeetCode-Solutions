class Solution(object):
    
    def splitArray(self, nums, k):
        
        def canSplit(nums, k, target):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > target:
                    count += 1
                    total = num
                    if count > k:
                        return False
            return True
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(nums, k, mid):
                right = mid
            else:
                left = mid + 1

        return left
    
        
