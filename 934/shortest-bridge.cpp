class Solution {
public:
    queue<int> queueI, queueJ, queueStep;
    int shortestBridge(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size();
        vector<vector<bool>> visited(M, vector<bool>(N, false));
        int ID = 2;
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(grid[i][j]==1) { //找到陸地，就逐一DFS 把它標示ID號碼
                    dfs(grid, i, j, ID++, visited);
                }
            }
        }
        
        //接下來，想從 island ID2 走到 island ID3
        vector<vector<bool>> visited2(M, vector<bool>(N, false));
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(grid[i][j]==2) {
                    queueI.push(i);
                    queueJ.push(j);
                    queueStep.push(0); //距離是0
                    visited2[i][j] = true;
                }
                printf("%d ", grid[i][j]);
            }
            printf("\n");
        }
        //答案，就是 BFS 算出的兩島的距離
        while(queueI.size()>0) {
            int i = queueI.front(), j = queueJ.front(), step = queueStep.front();
            if(grid[i][j] == 3) return step-1; //從 island 2 走到 island 3, 有答案了

            queueI.pop();
            queueJ.pop();
            queueStep.pop();
            bfs2(grid, i+1, j, step+1, visited2);
            bfs2(grid, i-1, j, step+1, visited2);
            bfs2(grid, i, j+1, step+1, visited2);
            bfs2(grid, i, j-1, step+1, visited2);
        }
        
        return 0;
    }
    void bfs2(vector<vector<int>>& grid, int i, int j, int step, vector<vector<bool>>&visited){
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size()) return;
        if(visited[i][j]) return;

        visited[i][j] = true;
        queueI.push(i);
        queueJ.push(j);
        queueStep.push(step);
    }
    void dfs(vector<vector<int>>& grid, int i, int j, int ID, vector<vector<bool>>&visited) {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size()) return;
        if(visited[i][j] || grid[i][j]==0) return;

        visited[i][j] = true;
        grid[i][j] = ID; //標示ID
        dfs(grid, i+1, j, ID, visited);
        dfs(grid, i-1, j, ID, visited);
        dfs(grid, i, j+1, ID, visited);
        dfs(grid, i, j-1, ID, visited);
    }
};
