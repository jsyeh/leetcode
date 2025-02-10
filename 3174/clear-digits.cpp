// LeetCode 3174. Clear Digits
// 從左到右，每次可把「數字」及它左邊的「字母」一起刪除，照著模擬即可
class Solution {
public:
    string clearDigits(string s) {
        vector<char> ans;
        for(char c : s) { // 左到右「逐字母」處理
            if(ans.size()>0 && isalpha(ans[ans.size()-1]) && isdigit(c)) {
                ans.pop_back(); // 左邊有字母、右邊是數字，就把左邊吐掉
            } else { // 沒辦法消掉的話
                ans.push_back(c); // 就乖乖把 c 塞進去
            }
        }
        return string(ans.begin(), ans.end()); // 把 vector<char> 轉成 string
    }
};
