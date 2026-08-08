class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m=grid.size();
        int n = grid[0].size();
        int forange=0;
        int time=0;
        queue<pair<int,int>>q;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1) forange++;
                else if(grid[i][j]==2) q.push({i,j});
            }
        }
        
        while(!q.empty() && forange>0){
            int x=q.size();
            time++;
            while(x){
                int a=q.front().first, b=q.front().second;
                
                q.pop();
                if(a-1>=0 && grid[a-1][b]==1){
                    grid[a-1][b]=2;
                    q.push({a-1,b});
                    forange--;
                } 
                if(b-1>=0 && grid[a][b-1]==1){
                    grid[a][b-1]=2;
                    q.push({a,b-1});
                    forange--;
                } 
                if(a+1<m && grid[a+1][b]==1){
                    grid[a+1][b]=2;
                    q.push({a+1,b});
                    forange--;
                } 
                if(b+1<n && grid[a][b+1]==1){
                    grid[a][b+1]=2;
                    q.push({a,b+1});
                    forange--;
                } 
                x--;
            }
        }
        if(forange!=0) return -1;
        return time;

    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna