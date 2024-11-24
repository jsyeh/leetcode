// LeetCode 1975. Maximum Matrix Sum
// 可把任2項相鄰的數「乘上-1」，問能做出「最大」的加總結果
// 要「加起來最大」，就是「儘量把負數變少」經過 Hint 1 和 Hint 
// 可推論：負數的位置，可「慢慢移動」到最小的那個數，或是全變正的
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int M = matrix.size(), N = matrix[0].size();
        int negative = 0;  // matrix 裡，有幾個負數
        long long totalAbs = 0, smallest = INT_MAX; // 答案加起來多少、最小值是誰
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(matrix[i][j]<0) { // 遇到負數
                    matrix[i][j] = -matrix[i][j]; // 就變正的
                    negative++; // 同時「負數」數目+1
                }
                totalAbs += matrix[i][j];  // 答案加起來多少
                if(matrix[i][j] < smallest) smallest = matrix[i][j]; // 更新最小值
            }
        }
        if(negative%2==1) return totalAbs - 2 * smallest; // 單數個「負數」，就挑最小的那個「犠牲」變負的
        return totalAbs;
    }
};
