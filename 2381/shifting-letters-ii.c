// LeetCode 2381. Shifting Letters II
// 給你字串 s，接下來「把某段」往上撥0 or 往下撥1，問最後的字串是什麼
char* shiftingLetters(char* s, int** shifts, int shiftsSize, int* shiftsColSize) {
    int N = strlen(s);
    int sh[N+1]; // 記錄累積「改變量」
    for(int i=0; i<N+1; i++) sh[i] = 0; // 在 C 語言，要手動把陣列「清為0」
    for(int i=0; i<shiftsSize; i++) {
        sh[shifts[i][0]] += shifts[i][2]*2-1; // 右邊可將 0, 1 換算成 -1, +1
        sh[shifts[i][1]+1] -= shifts[i][2]*2-1;
    }
    int d2 = 0;
    for(int i=0; i<N; i++) {
        d2 += sh[i]; // 照「改變量」累積
        s[i] = (((s[i]-'a') + d2) % 26 + 26) % 26 + 'a';
    }
    return s;
}

