int appendCharacters(char* s, char* t) {
    int N = strlen(t);  // 先知道「右邊t」的長度是多少
    int j = 0;  // t[j] 用在右邊的index
    for(int i=0; s[i]!=0; i++) {  // 字串 s 的 for 迴圈
        if(s[i]==t[j]) {  // 若相同，便又「收集」到1個字母
            j++;
            if(j==N) return 0;  // 若字母收齊，就成功了，答案就是0
        }
    }
    return N - j;  // 若沒收齊，看差幾個字母，就是答案
}
