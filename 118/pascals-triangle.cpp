class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans(numRows, vector<int>());
        ans[0].resize(1);
        ans[0][0] = 1;
        for(int i=1; i<numRows; i++) {
            ans[i].resize(i+1);
            ans[i][0] = 1; //左邊的1
            for(int j=1; j<i; j++){
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j];
            }
            ans[i][i] = 1; //右邊的1
        }
        return ans;
    }
};
