// LeetCode 766. Toeplitz Matrix
// 矩陣的「每一條斜線」值都相同，叫 Toeplitz 矩陣。檢試 matrix 是不是
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int M = matrix.size(), N = matrix[0].size();
        for(int i=0; i<M-1; i++) {
            for(int j=0; j<N-1; j++) {
                if(matrix[i][j] != matrix[i+1][j+1]) { // 若斜線不相同
                    return false; // 就不是
                }
            }
        }
        return true; // 成功檢測完，就是！
    }
};
