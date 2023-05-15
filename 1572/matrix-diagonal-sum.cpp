class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int N = mat.size();
        int ans = 0;
        for(int i=0; i<N; i++){
            ans += mat[i][i];
            if(i!=N-1-i) ans += mat[i][N-1-i];
        }
        return ans;
    }
};
