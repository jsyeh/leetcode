void reverseString(char* s, int sSize) {
    for(int i=0; i<sSize/2; i++){  // 迴圈執行「一半」，剛好換完
        int temp = s[i];  // 交換2個數，要寫3行
        s[i] = s[sSize-1-i];  // 可想像「兩杯水」要交換時
        s[sSize-1-i] = temp;  // 需要第3個「空杯子」暫放
    }  // 交換 s[i] 及 倒數的 s[N-1-i] 的意思
}
