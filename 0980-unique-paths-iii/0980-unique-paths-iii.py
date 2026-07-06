class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
     r=len(grid)
     c=len(grid[0])
     m=r*c
     wal=0
     ma=0
     for i in range(r):
                for j in range(c):
                    if grid[i][j]==1:
                        x,y=i,j
                    elif grid[i][j]==-1:
                        wal+=1
     so=[[0]*len(grid[0]) for i in grid]
 
     def sol(i,j,so,count):
       nonlocal ma
       if i<0 or j<0 or i>=r or j>=c or so[i][j] ==1 or grid[i][j]==-1:
           return 
       so[i][j]=1
       if grid[i][j]==2:
         if count==m-wal:
           ma+=1
         so[i][j]=0
         return
       sol(i+1,j,so,count+1)
       sol(i-1,j,so,count+1)
       sol(i,j+1,so,count+1)
       sol(i,j-1,so,count+1)
       so[i][j]=0
     sol(x,y,so,1)
     return ma