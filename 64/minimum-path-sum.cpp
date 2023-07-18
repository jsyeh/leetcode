class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size();
        int table[M][N];
        if(grid[0][0]==1) return 0;

        table[0][0]=1;
        for(int i=1; i<M; i++){
            if(grid[i][0]==1) table[i][0] = 0;
            else table[i][0] = table[i-1][0];
        }
        for(int j=1; j<N; j++){
            if(grid[0][j]==1) table[0][j] = 0;
            else table[0][j] = table[0][j-1];
        }

        for(int i=1; i<M; i++){
            for(int j=1; j<N; j++){
                if(grid[i][j]==1) table[i][j]=0;
                else table[i][j] = table[i-1][j] + table[i][j-1];
            }
        }
        return table[M-1][N-1];
    }
};
//case 36/41: [[1]]
