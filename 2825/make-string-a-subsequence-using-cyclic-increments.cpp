// LeetCode 2825. Make String a Subsequence Using Cyclic Increments
// str1 裡的字母，能不能配對出 str2 裡的字母 （配對是：相同 or +1）
class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        int N1 = str1.length(), N2 = str2.length();
        for(int i=0, j=0; i<N1; i++) {
            if(str1[i]==str2[j]) j++;
            else if((str1[i]-'a'+1)%26==str2[j]-'a') j++;
            if(j==N2) return true;
        }
        return false;
    }
};
