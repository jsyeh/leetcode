class Solution {
public:
    queue<int> ii;//i-coordinate
    queue<int> jj;//j-coordinate
    queue<int> dd;//distance
    int maxDistance(vector<vector<int>>& grid) {
        int land = 0, water = 0;
        for(int i=0; i<grid.size(); i++) {
            for(int j=0; j<grid[0].size(); j++) {
                if(grid[i][j]==1) {
                    land++;
                    ii.push(i);
                    jj.push(j);
                    dd.push(0);
                }else water++;
            }
        }
        if(land==0) return -1;//題目說: If no land or water exists in the grid, return -1.
        if(water==0) return -1;

        int ans = 0;
        while(ii.size()>0) {
            int i = ii.front(); ii.pop();
            int j = jj.front(); jj.pop();
            int d = dd.front(); dd.pop();
            helper(grid, i+1, j, d+1);
            helper(grid, i-1, j, d+1);
            helper(grid, i, j+1, d+1);
            helper(grid, i, j-1, d+1);
            ans = d;
        }
        return ans;
    }

    void helper(vector<vector<int>>& grid, int i, int j, int d) {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size()) return;
        if(grid[i][j]!=0) return  ;

        grid[i][j] = -1; //used
        ii.push(i);
        jj.push(j);
        dd.push(d);
    }
};
//case 36/38: [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
