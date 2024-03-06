class Solution(object):

    def exist( self, board, word):
            """
            :type board: List[List[str]]
            :type word: str
            :rtype: bool
            """
            def found(i, j, k, existii):
                if (k == len(word)):
                    return True
                if ((i < 0 or i == len(board))) or (j <0 or j==len(board[0])):
                    return False
                if ((board[i][j] != word[k])):
                    return False
                if (i, j) in existii:
                    return False
                existi = existii.copy()
                existi.add((i, j))
                return(found(i+1,j, k+1, existi) or found(i, j+1, k+1,existi) or found(i-1, j, k+1, existi) or found(i, j-1, k+1, existi))
            for i in range(len(board)):
                for j in range(len(board[0])):
                    exist = set()
                    if (found(i, j, 0, exist)):
                        return True
            return False             