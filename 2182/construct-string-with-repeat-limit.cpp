// LeetCode 2182. Construct String With Repeat Limit
// 用字串 s 的字母（不需全用），做出「新字串」，裡面字母不能重覆太多 （字母序要最大）
class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        int freq[128] = {}; // 統計字母出現次數
        for(char c : s) freq[c]++; 

        char ans[s.length()+1]; // 答案，使用 C 的字串，字串長度要+1
        int N = 0; // 答案（目前的）長度
        for(char c='z'; ; ) { // 字母大到小，依序處理
            c = 'z';
            while(c>='a' && freq[c]==0) c--; // c 是「最大的」字母
            if(c=='a'-1) break; //用盡了，就提早結束
            if(freq[c]>0) {
                int repeat = min(freq[c], repeatLimit);
                for(int k=0; k<repeat; k++) ans[N++] = c;
                freq[c] -= repeat;
            }
            if(freq[c]==0) continue; // 「最大的」字母用盡，可直接換下一顁
            char c2 = c-1; // c2 是「第二大」的字母
            while(c2>='a' && freq[c2]==0) c2--; // c2 是「第二大」的字母
            if(c2=='a'-1) break; //用盡了，就提早結束
            ans[N++] = c2;
            freq[c2]--;
        }
        ans[N] = 0; // 字串結尾
        return string(ans);
    }
};
