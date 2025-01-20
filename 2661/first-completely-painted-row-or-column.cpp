// LeetCode 2661. First Completely Painted Row or Column
// 照著 arr[k] 順序將mat對應格子著色，當k是多少時, 剛好將某條 row 或 col 全部著色
class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int M = mat.size(), N = mat[0].size();
        vector<int> I(M*N+1), J(M*N+1); // 用陣列「記錄對應的座標」
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                I[mat[i][j]] = i; // 先做 i,j 對照表
                J[mat[i][j]] = j;
            }
        }
        vector<int> rows(M), cols(N); // 可快速確認「是否集滿整條」
        for(int k=0; k<arr.size(); k++) {
            int i = I[arr[k]], j = J[arr[k]]; // 查回它對應的 i,j 座標
            rows[i]++;
            cols[j]++;
            if(rows[i]==N || cols[j]==M) return k;
        }
        return -1; // 不會執行到這行
    }
};
