// LeetCode 1544. Make The String Great
// 字串裡有大小寫的字母。相鄰2個字母若是大小寫不同的同一字母（ASCII剛好差32），就可消掉
// 一直消、一直消，直到不能消為止。回傳字串。
char* makeGood(char* s) {
    char a[101]; // 放答案的字元陣列（字串），最後會再放回s裡。若想加速，也可直接在s[i]做全部動作。
    int N = 0; // 目前 a 裡面，放了幾個字母（對應字串的長度）
    for(int i=0; s[i]!=0; i++) { // 把 s 裡，每個字母，逐個處理
        // 字串的 for 迴圈，中間s[i]!=0 表示「還沒到字串結尾」就一直做
        a[N] = s[i]; // 把現在的字母 s[i] 塞到 a[]的最後面
        if(N>=1) { // 原本a[] 裡有1個以上，現在再塞1個，就湊足2個，可檢查「能不能對消」
            if(a[N]-a[N-1]==32 || a[N-1]-a[N]==32) { // ASCII差32，剛好是「同字母」的大小寫
                N -= 2; // 就刪掉2個字母，下次會在2格前的位置繼續
            }
        }
        N += 1; // 前面第9行塞好 a[N] = s[i] 後，可換「下一格」
    }
    a[N] = 0; //將a的最後塞入「字串結尾」的符號 '\0' 完成最後處理
    strcpy(s, a); //把答案塞回 s，就不用自己準備memroy了。若想加速，也可直接在s[i]做全部動作。
    return s; //把答案 return 出來。
}
