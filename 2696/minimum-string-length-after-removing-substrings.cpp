// LeetCode 2696. Minimum String Length After Removing Substrings
// 可把 "AB" 或 "CD" 刪除，問字串s最後可變多短？
class Solution {
public:
    int minLength(string s) {
        vector<char> ans;  // 用來放「最後」刪除後的結果
        for(char c : s){  // 逐字母處理
            ans.push_back(c);  // 推進去
            int N = ans.size();
            if(N>=2){ // 長度夠長
                if(ans[N-2]=='A' && ans[N-1]=='B'){ // 符合條件
                    ans.pop_back(); // 就可以吐出來
                    ans.pop_back();
                }else if(ans[N-2]=='C' && ans[N-1]=='D'){ // 符合條件
                    ans.pop_back(); // 就可以吐出來
                    ans.pop_back();
                }
            }
        }
        return ans.size();
    }
};
