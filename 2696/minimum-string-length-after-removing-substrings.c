// LeetCode 2696. Minimum String Length After Removing Substrings
// 可把 "AB" 或 "CD" 刪除，問字串s最後可變多短？
int minLength(char * s){
    int N = 0;  // 直接在 s[i] 裡處理
    for(int i=0; s[i]!=0; i++){ // 字串的迴圈
        s[N++] = s[i]; // 塞入1個字母 （使用原本的陣列）
        if(N>=2){
            if(s[N-2]=='A' && s[N-1]=='B'){
                N-=2; // 吐出2個字母
            }else if(s[N-2]=='C' && s[N-1]=='D'){
                N-=2; // 吐出2個字母
            }
        }
    }
    return N;
}
