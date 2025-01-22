// LeetCode 2852. Sum of Remoteness of All Cells
// R[i][j] 是把遠離的「格子」加起來。要把 R[i][j] 全部加起來
// 等價於： total * totalCount, 再把每群「相連格子的和」*「相連格子數量」減掉
class Solution {
public:
    long long sumRemoteness(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid[0].size(); // 長、寬
        long long total = 0, totalCount = 0;  // non-blocks 的總和、有幾個
        long long ans = 0; // 最後的答案 = total * totalCount 再減掉「每群的和」*「對應格子數」
        int di[4] = {0,1,0,-1}, dj[4] = {1,0,-1,0};
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(grid[i][j]==-1) continue; // 避開 blocked 的格子
                total += grid[i][j]; // 更新 non-blocked 的總和
                totalCount++; // 更新 non-blocked 的格子數量
                long long now = grid[i][j]; // 現在這塊的 sum 是多少（先有自己這格的值）
                long long int count = 1; // 現在這塊有幾個格子（先有自己的這格）
                grid[i][j] = -1; // 走過，標示不要再走
                queue<pair<int,int>> Q; // 利用 queue 進行 BFS
                Q.push({i,j});
                while(Q.size()>0) {
                    int i0 = Q.front().first, j0 = Q.front().second;
                    Q.pop();
                    for(int k=0; k<4; k++) {
                        int ii = i0 + di[k], jj = j0 + dj[k]; // 四方向的鄰居
                        if(ii<0 || jj<0 || ii>=M || jj>=N || grid[ii][jj]==-1) continue;
                        total += grid[ii][jj];
                        totalCount++;
                        now += grid[ii][jj];
                        count++;
                        grid[ii][jj] = -1; // 標示 blocked 代表「走過」就不要再走
                        Q.push({ii,jj});
                    }
                }
                ans -= now * count; // 要減掉「這群的和」*「這群的數量」
            }
        }
        ans += total * totalCount; // 最後（有了準確的total及totalCount後）再補加「全部」的部分
        return ans;
    }
};
