// LeetCode 2168. Unique Substrings With Equal Digit Frequency
// 想看看 substring 裡，有幾個「出現的數字頻率都相同」
// 字串長度<=1000，可用暴力法來巡
class Solution {
public:
    int equalDigitFrequency(string s) {
        unordered_set<string> ans;
        for(int i=0; i<s.length(); i++) { // 字串開始位置 i
            int freq[10] = {}, maxf = 0, fN = 0;
            for(int j=i; j<s.length(); j++) { // 字串結束位置 j
                int now = s[j]-'0';
                if(freq[now]==0) fN++; // 多使用1個新字母
                freq[now]++;
                maxf = max(maxf, freq[now]); // 字母使用的最大頻率
                if(j-i+1==maxf*fN) ans.insert(s.substr(i,j-i+1));
            } // 每個人都是最大的頻率，代表出現頻率相同
        }
        return ans.size();
    }
};

