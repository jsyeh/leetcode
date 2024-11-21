// LeetCode 2257. Count Unguarded Cells in the Grid
// G 是 Guard, W 是 Wall, 問 m x n 有幾個格子「不會被 Guard 看到」
class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        int grid[m][n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                grid[i][j] = 0;
            }
        }
        for(int k=0; k<guards.size(); k++){
            int i = guards[k][0], j = guards[k][1];
            grid[i][j] = 1;
        }
        for(int k=0; k<walls.size(); k++){
            int i = walls[k][0], j = walls[k][1];
            grid[i][j] = 1;
        }
        for(int k=0; k<guards.size(); k++){
            int i = guards[k][0], j = guards[k][1];
            for(int kk=i+1; kk<m; kk++){
                if(grid[kk][j]==1) break;
                grid[kk][j] = 2;
            }
            for(int kk=i-1; kk>=0; kk--){
                if(grid[kk][j]==1) break;
                grid[kk][j] = 2;
            }
            for(int kk=j+1; kk<n; kk++){
                if(grid[i][kk]==1) break;
                grid[i][kk] = 2;
            }
            for(int kk=j-1; kk>=0; kk--){
                if(grid[i][kk]==1) break;
                grid[i][kk] = 2;
            }
        }
        int ans = 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j]==0) ans++;
            }
        }
        return ans;
    }
};
