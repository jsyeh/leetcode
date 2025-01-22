// LeetCode 1765. Map of Highest Peak
// isWater[i][j] 陸地0、海洋1，希望從海平面開始「一步步變高」重建對應的「高度地圖」
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int M = isWater.size(), N = isWater[0].size();
        vector<vector<int>> ans(M, vector<int>(N,-1)); // 答案（要重建出高度地圖），始始值 -1
        queue<vector<int>> Q; // 利用 queue 進行 BFS 依序探索重建「高度地圖」
        for(int i=0; i<M; i++) { // 先巡一次 isWater[i][j]
            for(int j=0; j<N; j++) {
                if(isWater[i][j]) { // 如果是水/海洋的話
                    ans[i][j] = 0; // 海平面「高度是0」
                    Q.push(vector<int>{0,i,j}); // 將海洋加入 queue, 對應高度是0
                }
            }
        }
        int di[4] = {0,1,0,-1}, dj[4] = {1,0,-1,0}; // 4個方向鄰居
        while(Q.size()>0) { //接下來，針對 queue 裡的高度、座標，依序處理
            int h = Q.front()[0], i = Q.front()[1], j = Q.front()[2];
            Q.pop();
            for(int k=0; k<4; k++) { // 4個方向鄰居
                int ii = i+di[k], jj = j+dj[k]; // 4個方向鄰居
                if(ii<0 || jj<0 || ii>=M || jj>=N) continue; // 超過範圍
                if(ans[ii][jj] != -1) continue; // 有處理過了，就不再處理
                ans[ii][jj] = h + 1; // 更新 (ii,jj) 的高度
                Q.push(vector<int>{h+1,ii,jj}); // 新的座標，也加入 queue 裡處理
            }
        }
        return ans;        
    }
};
