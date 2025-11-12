// LeetCode 54. Spiral Matrix
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) { // 使用牆壁的技巧,撞到牆,就換方向
        int M=matrix.size(), N=matrix[0].size();
        int top=0, bottom=M-1, left=0, right=N-1;// 我們的上下左右的可行範圍
        vector<int> ans;
        while (top<=bottom && left<=right) { // 還在範圍內,有機會
            for (int j=left; j<=right; j++) ans.push_back(matrix[top][j]); // 最上的列,往右走
            top++; // 邊界往下掉

            for (int i=top; i<=bottom; i++) ans.push_back(matrix[i][right]); // 最右的行,往下走
            right--; // 邊界往左收
            if( ! (top<=bottom && left<=right) ) break; // 「不」在範圍內,就要離開

            for (int j=right; j>=left; j--) ans.push_back(matrix[bottom][j]); // 最下的列,往左走
            bottom--;
            
            for (int i=bottom; i>=top; i--) ans.push_back(matrix[i][left]); // 最左的行,往上走
            left++;
        }
        return ans;
    }
};
