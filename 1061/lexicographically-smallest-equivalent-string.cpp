// LeetCode 1061. Lexicographically Smallest Equivalent String
// s1 s2 的對應字母相同，即 s1[i] 和 s2[i] 的字母是「等價」的。
// 把 baseStr 變成「對應等價」的最小字母的字中
class Solution {
public:
    char find(char c) { // 與 table 配合，能找到「等價」最小的字母
        if(table[c]==table[table[c]]) return table[c]; // 最大的最大，已是最大
        table[c] = find(table[c]);
        return table[c];
    }
    char table[256];
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        for(char c='a'; c<='z'; c++) table[c] = c; // 先自己對應自己
        for(int i=0; i<s1.length(); i++) { // 由 s1 s2 建出對照表
            char c1 = s1[i], c2 = s2[i];
            char d1 = find(c1), d2 = find(c2); // 再函式呼叫函式，更新
            if(d1<d2) table[d2] = d1; // 找到最小的，存起來
            else table[d1] = d2;
        }
        string ans(baseStr.length(), ' '); // 準備好答案
        for(int i=0; i<baseStr.length(); i++) {
            ans[i] = find(baseStr[i]);
        }
        return ans;
    }
};
