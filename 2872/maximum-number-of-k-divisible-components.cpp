// LeetCode 2872. Maximum Number of K-Divisible Components
// 把 tree 斷開成很多個「小樹」，小樹的node加起來必須是 k 的倍數。最多可分成幾個「小樹」？
class Solution {
public:
    int ans = 0; // 目前剪掉的樹的次數
    long long int helper(int i, vector<int>& values, int k, vector<vector<int>>& path, vector<bool>& visited) {
        long long int total = values[i]; // 目前的總合
        visited[i] = true; // 標示「走過」
        for(auto i2 : path[i]) { // 針對「相鄰」的node，是不是subtree呢？
            if(visited[i2]) continue; // 走過，就不要再走
            long long int now = helper(i2, values, k, path, visited); // 函式呼叫函式
            if(now%k==0) ans++; // 合乎題目要求，可以剪掉，答案+1
            else total += now; // 無法剪掉的，合併在上面
        }
        return total; // 這個 subtree 還沒被剪掉的 total 總合
    }
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        vector<vector<int>> path(n); // 先照著 edges 結構，建出 path 資訊
        for(auto edge : edges) { // 依照 edge 建出「相鄰路徑」的關係
            int a = edge[0], b = edge[1];
            path[a].push_back(b); // a 可以到 b
            path[b].push_back(a); // b 可以到 a
        }
        vector<bool> visited = vector<bool>(n);
        ans = 0; // 目前剪掉的樹的次數
        helper(0, values, k, path, visited);
        return ans + 1; // 加上沒有剪掉的主枝，總共有 self.ans + 1 個樹
    }
};
