class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q=deque()
        m=len(image)
        n=len(image[0])
        start_color=image[sr][sc]
        if start_color==color:
            return image
        image[sr][sc]=color
        q.append((sr,sc))
        
        while q:
            x=len(q)
            while(x):
                a,b=q.popleft()
                dx,dy=[1,0,-1,0],[0,1,0,-1]
                for i in range(4):
                    nx=a+dx[i]
                    ny=b+dy[i]
                    if nx<0 or nx>=m or ny<0 or ny>=n:
                        continue
                    if image[nx][ny]==start_color:
                        image[nx][ny]=color
                        q.append((nx,ny))
                x-=1
        return image

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna