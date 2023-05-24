class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        //想法: 每次轉動90度,如果完全符合, 便true,不然就false
        int N = mat.size();
        for(int k=0; k<4; k++) {
            //可利用前一題 48. Rotate Image 的 in-place 的旋轉, 方便做4次
            rotate(mat);
            if(compare(mat, target)==true) return true;
        }
        return false;
    }
    void rotate(vector<vector<int>>&matrix) {
        int N = matrix.size();
        for(int i=0; i<N/2; i++) {//可利用前一題 48. Rotate Image 的 in-place 的旋轉
            for(int j=0; j<(N+1)/2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[N-1-j][i];
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j];
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i];
                matrix[j][N-1-i] = temp;
            }
        }
    }
    bool compare(vector<vector<int>>&mat, vector<vector<int>>&target) {
        int N = mat.size();
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(mat[i][j] != target[i][j]) return false;
            }
        }
        return true;
    }
};
