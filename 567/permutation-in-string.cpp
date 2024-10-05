// LeetCode 567. Permutation in String
// 問 s1 能不能是 s2子字串 的排列組合（有相同數目的字母）
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int H[256] = {}; // 統計字母出現的次數
        int N1 = s1.length(), N2 = s2.length();
        if(N1>N2) return false; // s2長度不夠，失敗
        for(char c : s1) H[c]++; // 先統計s1的字母出現次數
        for(int i=0; i<N1; i++) H[s2[i]]--; // 用掉字母

        int match = 0; // 為了節省時間，用 match 儲存「有幾個字母相同」
        for(int i='a'; i<='z'; i++){
            if(H[i]==0) match++; // 剛好用完字母，代表「字母相同」
        }
        if(match==26) return true; // 剛好26種字母的數目都相同，成功

        for(int i=N1; i<N2; i++){ // 利用毛毛蟲法，處理剩下的字母
            char c = s2[i], c2 = s2[i-N1]; // 毛毛蟲法，右邊字母c,左邊字母c2
            H[c]--; // 吃入字母c，也就是再用掉字母c
            if(H[c]==0) match++;
            else if(H[c]==-1) match--;
            H[c2]++; // 吐出字母c2，也就是回補字母c2
            if(H[c2]==0) match++;
            else if(H[c2]==1) match--;
            if(match==26) return true; // 剛好26種字母的數目都相同，成功
            
        }
        return false;
    }
};
