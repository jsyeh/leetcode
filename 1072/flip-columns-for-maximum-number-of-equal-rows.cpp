// LeetCode 1072. Flip Columns For Maximum Number of Equal Rows
// 以 row 為單位，看有沒有重覆的形狀。形狀重覆，就能一起轉換成「全0」「全1」
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        // 因無法用 vector<int> 當成 unordered_map 的 key 所以改成字串
        int ans = 0;
        unordered_map<string, int> counter;
        for(auto row : matrix) {
            string s = "";  // 把 row 轉換成 字串
            if(row[0]==1){ // 開頭是1，就手動轉成「開頭是0」的版本
                for(int i=0; i<row.size(); i++) s += '0' + 1-row[i]; 
            }else{ // row 的一堆整數，變成一堆 '0' '1' 的字串
                for(int i=0; i<row.size(); i++) s += '0' + row[i];
            }
            counter[s]++; // 把 row 對應的字串，記錄起來，數量+1
            ans = max(ans, counter[s]); // 更新答案
        }
        return ans;
    }
};
