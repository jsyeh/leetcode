// LeetCode 1684. Count the Number of Consistent Strings
// 數數看 words 裡, 有幾個 word 是好的(也就是裡面每個字母,都是 allowed)
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        bool good[256] = {}; // 建一個 good 的對照表, {} 預設值是 false (ASCII 有 256個字母)
        for(char c : allowed) good[c] = true; // 如果是 allowed 裡的字, good[c] 設成好的
        int ans = 0; // 要統計有幾個好的
        for(string word : words){
            bool bad = false; // 迴圈前面 bad 是 false 還沒壞
            for(char c : word){
                if(good[c]==false){ // 迴圈裡面, 發現有「不好」的字母
                    bad = true;  // 那就不好了、壞掉
                }
            }
            if(bad==false) ans++; // 迴圈後面,檢查 bad 嗎? 沒有壞掉, 就多找到一個答案
        }
        return ans;
    }
};
