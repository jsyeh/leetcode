class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {
        for(int i=0; i<grid.size(); i++){
            helper(grid, i, 0);
            helper(grid, i, grid[0].size()-1);
        }
        for(int j=0; j<grid[0].size(); j++){
            helper(grid, 0, j);
            helper(grid, grid.size()-1, j);
        }

        int ans=0;
        for(int i=0; i<grid.size(); i++){
            for(int j=0; j<grid[0].size(); j++){
                if(grid[i][j]==1) ans++;
            }
        }
        return ans;
    }
    void helper(vector<vector<int>>&grid, int i, int j) {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size()) return;
        if(grid[i][j]==0) return;

        grid[i][j] = 0;
        helper(grid, i+1, j);
        helper(grid, i-1, j);
        helper(grid, i, j+1);
        helper(grid, i, j-1);
    }
};
