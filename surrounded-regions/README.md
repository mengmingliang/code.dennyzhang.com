# Leetcode: Surrounded Regions     :BLOG:Medium:


---

Surrounded Regions  

---

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.  

A region is captured by flipping all 'O's into 'X's in that surrounded region.  

    For example,
    X X X X
    X O O X
    X X O X
    X O X X
    After running your function, the board should be:
    
    X X X X
    X X X X
    X X X X
    X O X X

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/surrounded-regions)  

Credits To: [leetcode.com](https://leetcode.com/problems/surrounded-regions/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/surrounded-regions
    ## Basic Ideas: Two kind of Os: 
    ##                 1 it will definitely not surrounded by 'X'
    ##                 2 it might or might not           
    ##
    ##              For case1, we mark it to 'Y'. Then go with DFS
    ##              After one pass, for positions of remaining O, they are all surrounded by 'X'
    ##                              for positions of all 'Y', they're fine
    ##
    ##             X    X    X    X    X
    ##             X    O    O    O    X
    ##             X    O    X    O    X
    ##             X    O    O    O    X
    ##             X    X    X    X    X
    ##             X    X    O    O    X
    ##             X    X    O    X    X
    ##
    ## Complexity: Time O(n*m), Space O(1)
    class Solution(object):
        def solve(self, board):
            """
            :type board: List[List[str]]
            :rtype: void Do not return anything, modify board in-place instead.
            """
            self.row_count = len(board)
            if self.row_count == 0: return
            self.col_count = len(board[0])
            for i in xrange(self.row_count):
                for j in xrange(self.col_count):
                    if board[i][j] == 'O':
                        self.DFSMark(board, i, j)
    
            # print board
            # change 'O' to 'X', change 'Y' to 'O'
            for i in xrange(self.row_count):
                for j in xrange(self.col_count):
                    if board[i][j] == 'O': board[i][j] = 'X'
                    if board[i][j] == 'Y': board[i][j] = 'O'
    
        def DFSMark(self, board, i, j):
            # out of bound
            if i < 0 or i >= self.row_count or \
                j < 0 or j >= self.col_count:
                    return
    
            # If the element is 'Y', we won't keep going neither.
            # This will save duplicate caculation
            if board[i][j] != 'O':
                return
    
            # base cases
            if i == 0 or i == self.row_count-1 or \
                j == 0 or j == self.col_count-1:
                    # Y indicates this position is definitely fine
                    board[i][j] = 'Y'
            else:
                # check whether the adjacent element has 'Y'
                if self.hasAdjacentY(board, i, j):
                    board[i][j] = 'Y'
                else:
                    return
            self.DFSMark(board, i-1, j)
            self.DFSMark(board, i+1, j)
            self.DFSMark(board, i, j-1)
            self.DFSMark(board, i, j+1)
    
        def hasAdjacentY(self, board, i, j):
            if i > 0 and board[i-1][j] == 'Y': return True
            if i < self.row_count-1 and board[i+1][j] == 'Y': return True
            if j > 0 and board[i][j-1] == 'Y': return True
            if j < self.col_count-1 and board[i][j+1] == 'Y': return True
            return False        
    
    s = Solution()
    # board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    board = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
    s.solve(board)