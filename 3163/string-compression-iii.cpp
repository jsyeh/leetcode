// LeetCode 3163. String Compression III
// 字串壓縮演算法：重覆的字母數量，放在字母前面（數量不能>9)
class Solution {
public:
    string compressedString(string word) {
        string ans; // 用來存放答案
        char prevC = word[0]; // 重覆的字母，一開始是 word[0]
        int prevN = 1; // 目前先有1個字母
        for(int i=1; i<word.length(); i++) { // 前面已用 word[0] ，故從1開始
            if(word[i]==prevC && prevN<9) { // 與前個字母相同，且不超過 9 個，就可累加
                prevN++; // 有可能「累加到9個」 
            } else { // 如果無法再累加，就要輸出「數字、字母」的組合
                ans += std::to_string(prevN) + prevC; // 輸出前面的「數量」及「字母」
                prevC = word[i]; // 換新的字母
                prevN = 1;
            }
        }
        ans += std::to_string(prevN) + prevC; // 塞最後一筆的答案
        return ans;        
    }
};
