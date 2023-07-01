class Solution {
public:
    queue<int> queueI, queueJ, queueDist;
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int M = mat.size(), N = mat[0].size();
        vector<vector<bool>> visited(M, vector<bool>(N, false));
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(mat[i][j]==0) { //遇到 0 的部分
                    queueI.push(i);
                    queueJ.push(j);
                    queueDist.push(0);
                    visited[i][j] = true;
                }
            }
        }
        while(queueI.size()>0) {
            int i = queueI.front(), j = queueJ.front(), dist = queueDist.front();
            queueI.pop();
            queueJ.pop();
            queueDist.pop();
            testAndPush(mat, i+1, j, dist, M, N, visited);
            testAndPush(mat, i-1, j, dist, M, N, visited);
            testAndPush(mat, i, j+1, dist, M, N, visited);
            testAndPush(mat, i, j-1, dist, M, N, visited);
        }
        return mat;
    }
    void testAndPush(vector<vector<int>>& mat, int i, int j, int dist, int M, int N, vector<vector<bool>>& visited) {
        //要小心，加入&才會傳參考
        if(i<0 || j<0 || i>=M || j>=N) return;
        if(visited[i][j]) return;

        visited[i][j] = true;
        mat[i][j] = dist + 1;
        queueI.push(i);
        queueJ.push(j);
        queueDist.push(dist+1);
    }
};
