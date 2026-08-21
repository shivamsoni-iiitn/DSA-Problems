class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        visited=[[0]*n for _ in range(m)] 
        q=deque()
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if grid[i][j]==1 and visited[i][j]==0:
                        visited[i][j]=1
                        q.append((i,j))
        dr,dc=[0,1,0,-1],[1,0,-1,0]
        while q:
            a,b=q.popleft()
            for i in range(4):
                nr,nc=a+dr[i], b+dc[i]
                if nr>=0 and nc>=0 and nr<m and nc<n and visited[nr][nc]==0 and grid[nr][nc]==1:
                    visited[nr][nc]=1
                    q.append((nr,nc))
        count=0
        for i in range(m):
            for j in range(n):
                if visited[i][j]==0 and grid[i][j]==1:
                    count+=1
        return count
                    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna