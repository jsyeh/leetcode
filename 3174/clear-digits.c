// LeetCode 3174. Clear Digits
// 把「第1個digit及其左邊的non-digit刪除」
char* clearDigits(char* s) {
    int k = 0; // s[k] 對應目前放答案的地方
    for(int i=1; s[i]!=0; i++) { //左邊s[k] 右邊s[i]
        if(k>=0 && isdigit(s[i]) && isalpha(s[k])){
            //因為字串只有「小寫子母、數字」所以用'-'代表刪除
            //s[i]='-'; //要刪
            //s[k]='-'; //要刪
            k--; //改成這樣，才正確
        }else{ //不要刪
            s[++k] = s[i];
        }//k增加後，把最新的字，放入 s[k]
    }
    s[k+1] = 0;
    return s;
}
