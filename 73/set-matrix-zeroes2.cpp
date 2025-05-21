// LeetCode 73. Set Matrix Zeroes
// 陣列 matrix 裡若 matrix[i][j] == 0 的話，就把對應的直行、橫行，都變成0
// 可以先在左邊、上面，準備2條長條的陣列，若 matrix[i][j]==0就把 left[i] 和 up[j] 打勾勾
// 最後再用迴圈，把有打勾勾的對應格子，都設成 0 即可
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int M = matrix.size(), N = matrix[0].size(); // 左M, 右N
        vector<int> left(M), up(N); // 左邊長條、上面長條的C++陣列
        for(int i=0; i<M; i++){ // 左手 i 範圍是 M
            for(int j=0; j<N; j++){ // 右手 j 範圍是 N
                if(matrix[i][j]==0){ // 遇到有0,就在左邊長條、上面長條打勾勾
                    left[i] = 7; // 打勾勾
                    up[j] = 7; // 打勾勾
                }
            }
        }
        for(int i=0; i<M; i++){ // 左手 i 範圍是 M
            for(int j=0; j<N; j++){ // 右手 j 範圍是 N
                if(left[i]==7 || up[j]==7) matrix[i][j] = 0;
            } // 遇到左邊有勾勾 or 上面有勾勾, 就把它設成0囉
        }        
    }
};
