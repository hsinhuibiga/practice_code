class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        import copy
        
        m = len(board)
        n = len(board[0])
        res=copy.deepcopy(board)
        def myzero(x,y):
            Direct = zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1])
            flag=0
            for dx,dy in Direct:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and res[nx][ny]==1:
                    flag+=1 
            return int(flag ==3) 
        def myone(x,y):
            flag=0
            Direct = zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1])
            for dx,dy in Direct:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and res[nx][ny]==1:
                    flag+=1 
            return int(flag ==3 or flag ==2)
        for x in range(m):
            for y in range(n):
                if res[x][y] == 0:
                    board[x][y] = myzero(x,y)
                else:
                    board[x][y] = myone(x,y)