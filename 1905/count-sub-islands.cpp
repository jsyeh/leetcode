class Solution {
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        //技巧: 染色,把 grid1 全部的 id 照著 ID 染色, 再把 grid2 做一樣的事,
        //同時檢查對應 grid1 的 id 是否都相同

        int ID = 2;
        for(int i=0; i<grid1.size(); i++) {
            for(int j=0; j<grid1[0].size(); j++) {
                if(grid1[i][j]==1) {
                    helper(grid1, i, j, ID); //1 變 ID
                    ID++;
                }
            }
        }
//printf("ID Part 1:%d\n", ID);
//show(grid1);
        int ans = 0;
        for(int i=0; i<grid2.size(); i++){
            for(int j=0; j<grid2[0].size(); j++){
                if(grid2[i][j]==1){
                    bool good = helper2(grid1, grid2, i, j, grid1[i][j], ID);
                    if(good && grid1[i][j]!=0) ans++;

                    ID++;
                }
            }
        }
//printf("ID Part 2:%d\n", ID);
//show(grid2);
        return ans;
    }

    void show(vector<vector<int>>grid) {
        for(int i=0; i<grid.size(); i++){
            for(int j=0; j<grid[0].size(); j++){
                printf("%d", grid[i][j]);
            }
            printf("\n");
        }
    }

    void helper(vector<vector<int>>& grid, int i, int j, int ID) {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size()) return;
        if(grid[i][j]!=1) return;

        grid[i][j] = ID;
        helper(grid, i+1, j, ID);
        helper(grid, i-1, j, ID);
        helper(grid, i, j+1, ID);
        helper(grid, i, j-1, ID);
    }

    bool helper2(vector<vector<int>>& grid1, vector<vector<int>>&grid2, int i, int j, int c1, int c2) {
        if(i<0 || j<0 || i>=grid1.size() || j>=grid1[0].size()) return true; //離開,沒事
        if(grid2[i][j]!=1) return true; //沒事

        grid2[i][j] = c2;

        int bad=0;
        if(grid1[i][j]!=c1) bad=1; //糟,對照的 grid1[i][j] 的值有不同,就不是sub-island

        if(!helper2(grid1, grid2, i+1, j, c1, c2)) bad=1;
        if(!helper2(grid1, grid2, i-1, j, c1, c2)) bad=1;
        if(!helper2(grid1, grid2, i, j+1, c1, c2)) bad=1;
        if(!helper2(grid1, grid2, i, j-1, c1, c2)) bad=1;

        if(bad==0) return true;
        else return false;
    }
};
