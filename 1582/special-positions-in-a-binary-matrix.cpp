// LeetCode 1582. Special Positions in a Binary Matrix
// 如果 mat[i][j]==1 而且 row[i]==1 及 col[i]==1 都是唯一
class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int M = mat.size(), N = mat[0].size(); // 矩陣的長、寬
        // 前面先統計每個 row 及每個 col 的1有幾個
        int row[100] = {}, col[100] = {}; // 一開都 row 和 col 都是 0
        for (int i=0; i<M; i++) { // 利用 for 迴圈「巡」每個格子
            for (int j=0; j<N; j++) {
                if (mat[i][j]==1) { // 若格子是1
                    row[i] ++; // 對應的 row +1
                    col[j] ++; // 對應的 col +1
                }
            }
        }
        // 後面再檢查一次, 符合row和col「都是唯一」的格子, 統計數量
        int ans = 0;
        for (int i=0; i<M; i++) {
            for (int j=0; j<N; j++) {
                if (mat[i][j]==1 && row[i]==1 && col[j]==1) ans += 1;
            }
        }
        return ans; // 回傳答案
    }
};
