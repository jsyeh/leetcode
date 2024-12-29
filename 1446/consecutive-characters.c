// LeetCode 1446. Consecutive Characters
// 字串 s 裡，相同字母連續最長的長度
int maxPower(char* s) {
    int ans = 1, prevN = 1;
    char prevC = s[0];
    for(int i=1; s[i]!=0; i++) {
        if(s[i]==prevC) {
            prevN++;
            if(prevN>ans) ans = prevN;
        } else {
            prevC = s[i];
            prevN = 1;
        }
    }
    return ans;
}
