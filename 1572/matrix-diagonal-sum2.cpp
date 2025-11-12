// LeetCode 1572. Matrix Diagonal Sum
// 有兩條對角線 左上、右下 (i==j) 另一條右上、左下(相加==N-1)
class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int ans = 0; // 對角線 加起來 的總合
        int N = mat.size();
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (i==j || i+j==N-1) ans += mat[i][j];
            }
        }
        return ans;
    }
};
