// LeetCode 1957. Delete Characters to Make Fancy String
// 「不可連續3個相同字母」的字串，要把 s 刪掉幾個字母才行？
// 就直接 for迴圈，如果重覆的字 < 3 就 ans.append(c) 放入答案
char* makeFancyString(char* s) {
    int prevC = 0, prevN = 0; // 之前出過的字母
    int N = 0; // 答案的字串長度
    for(int i=0; s[i]!=0; i++) { // 逐個字母處理
        if(s[i]==prevC){ // 有相同時，累加
            prevN++; // 次數+1
        } else { // 不相同時，換新的字母
            prevC = s[i];  // 換新的字母
            prevN = 1;  // 次數變1個
        }
        if(prevN < 3) s[N++] = s[i]; // 只要不超過3個，就可加入
    }
    s[N] = 0;
    return s;
}
