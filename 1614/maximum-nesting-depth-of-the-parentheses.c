// LeetCode 1614. Maximum Nesting Depth of the Parentheses
// 找出「括號」最深有幾層。就照著字串讀取，即時修正層數 d
// 如果層數 d 比 ans 大，就更新 ans
int maxDepth(char* s) {
    int ans=0, d=0;
    for(int i=0; s[i]!=0; i++){ // 字串的迴圈
        if(s[i]=='(') d++; // 讀到括號開始，層數就增加
        else if(s[i]==')') d--; // 讀到括號結束，層數就減少
        
        if(d>ans) ans = d; //如果層數 d 更大，就更新 ans
    }
    return ans;
}
