class Solution(object):
    def searchMatrix(self, matrix, target):
        l, r = 0, len(matrix)-1
        while(l<=r):
            m = (l+r)//2
            if(matrix[m][0]>target):
                r = m - 1
            elif(matrix[m][-1]<target):
                l = m +1
            else:
                break
        l, r = 0, len(matrix[0]) - 1
        if(l>r):
            return False
        while(l<=r):
            mid = (l+r)//2
            if(target<matrix[m][mid]):
                r = mid -1
            elif(target>matrix[m][mid]):
                l = mid + 1
            else:
                return True
        return False
    
        