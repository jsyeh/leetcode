// LeetCode 73. Set Matrix Zeroes
// 直覺寫出來的答案「是錯的」,因為0蔓延之後,變太多0了
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int M = matrix.size(), N = matrix[0].size();
        vector<int> up(N); //宣告一個陣列, 是放在上面up、用來「打勾勾」標注「有哪幾直條要刪」
        vector<int> left(M); //宣告一個陣列, 是放在左邊left、用來「打勾勾」標注「有哪幾橫條要刪」
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                if(matrix[i][j]==0){ //遇到0的話, 要標注 left[i] 和 up[j]
                    up[j] = 1;
                    left[i] = 1;
                }
            }
        }
        for(int i=0; i<M; i++){ //最後再把它變成0
            if(left[i]==1) for(int jj=0; jj<N; jj++) matrix[i][jj]=0; //如果左邊有「打勾勾」,就整條刪 橫條
        }
        for(int j=0; j<N; j++){
            if(up[j]==1) for(int ii=0; ii<M; ii++) matrix[ii][j]=0; //如果上面有「打勾勾」,就整條刪 直條
        }
    }
};
