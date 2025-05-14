// LeetCode 3335. Total Characters in String After Transformations I
// 'a'會變'b', 'b'會變'c' ... 'z'會變2個字母 'a' 和 'b'
class Solution {
public:
    int a[200000] = {}; // 很大的陣列, 裡面都是0 會放算出來的答案
    int helper(int t) { // 使用「函式呼叫函式」
        if( a[t] > 0 ) return a[t]; // 有放答案,就把答案直接拿來用
        if( t<26 ) return 1; // 還是1個字母
        a[t] = (helper(t-26) + helper(t-26+1)) % 1000000007; //  裡面有8個0
        return a[t];
    }
    int lengthAfterTransformations(string s, int t) {
        int ans = 0;
        for(char c : s) { // C++ 的語法, 可以把每個字母取出來
            ans = ( ans + helper( t + c-'a' ) ) % 1000000007; // 裡面有8個0
        }
        return ans;
    }
};
