class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0;
        for(int i=0; i<grid.size(); i++) {
            for(int j=0; j<grid[i].size(); j++) {
                if(grid[i][j]!=0) {
                    int temp = helper(grid, i, j);
                    if(temp>ans) ans = temp;
                }
            }
        }
        return ans;
    }
    int total = 0;
    int helper(vector<vector<int>>&grid, int i, int j) {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size()) return 0;

        if(grid[i][j]==0) return 0;
        else grid[i][j] = 0;

        int ans = 1;
        ans += helper(grid, i+1, j);
        ans += helper(grid, i-1, j);
        ans += helper(grid, i, j+1);
        ans += helper(grid, i, j-1);
        return ans;
    }
};
