// LeetCode 1730. Shortest Path to Get Food
// grid 裡 * 是你的位置，# 是食物，X 會卡住，能走 O，最快吃到食物
class Solution {
public:
    int getFood(vector<vector<char>>& grid) {
        // 使用 BFS 就可找到答案
        queue<vector<int>> Q; // BFS 的 queue 資料結構
        unordered_set<int> visited; // 走過的格子
        int M = grid.size(), N = grid[0].size(); // 長寬
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(grid[i][j]=='*') {
                    Q.push(vector<int>{0,i,j}); // 起點，0步
                    visited.insert(i*N+j); // 標示走過
                }
            }
        }
        int di[4] = {0,1,0,-1}, dj[4] = {1,0,-1,0}; // 右、下、左、上
        while(Q.size()>0) { // 還能 BFS 的話
            int step = Q.front()[0], i = Q.front()[1], j = Q.front()[2]; // 現在在哪裡
            Q.pop(); // 用完、吐掉
            
            for(int d=0; d<4; d++) { // 往右、下、左、上 4個方向試
                int ii = i+di[d], jj = j+dj[d];
                if(ii<0 || jj<0 || ii>=M || jj>=N) continue; // 超過邊界，避開
                if(grid[ii][jj]=='#') return step + 1; // 找到食物，太好了
                if(grid[ii][jj]=='X' || visited.count(ii*N+jj)) continue; // 不能走 or 走過，避開
                Q.push(vector<int>{step+1,ii,jj});
                visited.insert(ii*N+jj);
            }
        }
        return -1; // 找不到食物
    }
};
