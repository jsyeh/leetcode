// LeetCode 2371. Minimize Maximum Value in a Grid
// grid有不同的正數。在不改變「在同row或col」相對關係，可換新值
// 要讓 grid 裡「最大的值」最小。Hint 2 建議：從小到大，慢慢降值
class Solution {
public:
    vector<vector<int>> minScore(vector<vector<int>>& grid) {
        priority_queue<pair<int,pair<int,int>>> heap;
        int M = grid.size(), N = grid[0].size();
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                heap.push(pair(-grid[i][j], pair(i,j)));
            }
        }
        vector<int> rowMax(M), colMax(N);
        while(heap.size()>0) {
            int oldVal = -heap.top().first;
            int i = heap.top().second.first, j = heap.top().second.second;
            int now = max(rowMax[i], colMax[j]) + 1;
            grid[i][j] = now;
            rowMax[i] = colMax[j] = now;
            heap.pop();
        }
        return grid;
    }
};
