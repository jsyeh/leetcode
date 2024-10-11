// LeetCode 1002. Find Common Characters
char ** commonChars(char ** words, int wordsSize, int* returnSize){
    char** ans = (char**) malloc(sizeof(char*)*100);  // 準備好答案需要的指標
    for(int i=0; i<100; i++){  // C 語言比較麻煩的是 memory管理, 要自己做
        ans[i] = (int*) malloc(sizeof(char)*2);  // 為每個字母(對應的字串), 準備好 memory
    } // 題目最多有 100 個字母
    int H[26] = {};  // 用來統計words[0] 的字母出現次數
    for(int k=0; words[0][k]!=0; k++){ // 統計 words[0] 裡的字母出現次數
        H[words[0][k]-'a']++; // 統計 words[0] 裡的字母出現次數
    }
    for(int i=1; i<wordsSize; i++) {
        int H2[26] = {};  // 用來統計words[i] 的字母出現次數
        for(int k=0; words[i][k]!=0; k++) { // 統計 words[i] 裡的字母出現次數
            H2[words[i][k]-'a']++;
        }
        for(int c=0; c<26; c++) { // 針對 26個字母, 逐一分析
            if(H2[c]<H[c]) H[c] = H2[c]; // 以比較少的出現次數為準
        }
    }
    int N = 0; // 最後算出答案
    for(int c=0; c<26; c++) { // 針對 26個字母
        for(int h=0; h<H[c]; h++) { // 針對出現次數, 重覆放字母
            ans[N][0] = c + 'a';  // 字母對的字串的前面那格
            ans[N][1] = '\0';  // 字母對應的字串的後面結束那格
            N++;
        }
    }
    *returnSize = N;
    return ans;
}
