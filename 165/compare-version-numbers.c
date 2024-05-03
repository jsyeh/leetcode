// LeetCode 165. Compare Version Numbers
// 「版本號碼」裡有數字、小數點, 像是 1.01 或 1.1.1 等
// 有兩個字串, 對應兩個版本號碼。比較兩個版本號碼，看看誰比較大：
// 如果左邊大, 就回傳1。右邊大, 就回傳-1。就很像 a-b 看正負號的意思
int compareVersion(char* version1, char* version2) {
    int v1[500] = {}, v2[500] = {};  // 預設值都是0
    int N1 = 0, N2 = 0;  // 對應兩個陣列的長度
    for(int i=0; version1[i]!=0; i++) {
        if(version1[i]=='.') N1++;  // 把字串, 用點斷開, 變陣列
        else v1[N1] = v1[N1] * 10 + (version1[i]-'0');
    }
    N1++;
    for(int i=0; version2[i]!=0; i++) {
        if(version2[i]=='.') N2++;  // 把字串, 用點斷開, 變陣列
        else v2[N2] = v2[N2] * 10 + (version2[i]-'0');
    }
    N2++;

    int N = (N1>N2) ? N1 : N2;
    for(int i=0; i<N; i++) {  // 逐個比較
        if(i<N1 && i<N2) {  // i 沒有超過兩個陣列的長度, 就一起比較
            if(v1[i]>v2[i]) return 1;
            if(v1[i]<v2[i]) return -1;
        }else if(i<N1 && v1[i]>0) return 1;  // 若左邊比較長 且有數字
        else if(i<N2 && v2[i]>0) return -1;  // 若右邊比較長, 且有數字
    }
    return 0;
}
