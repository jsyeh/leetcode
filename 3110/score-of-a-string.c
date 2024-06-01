// LeetCode 3110. Score of a String
// 今天的挑戰題，是要算一下「字串」對應的分數。
// 把「相鄰的字母的ASCII值的差」，全部加起來，就是答案了
int scoreOfString(char* s) {
    int ans = 0;  // 迴圈前面 ans 是0
    for(int i=0; s[i+1]!=0; i++){  // 修改後的字串迴圈，方便「兩兩比較」
        ans += abs(s[i+1]-s[i]);  // 迴圈中間，更新 ans
    }
    return ans;  // 迴圈後面，把答案拿來用
}
