//判斷 word1 word2 是否 close: 字母位置可換、字母值可對換
int comp(const void*p1, const void*p2){ //qsort()用
    return *(int*)p1 - *(int*)p2; //可照出現次數排序
}
bool closeStrings(char* word1, char* word2) {
    int H1[26]={}, H2[26]={}; //統計字母出現次數
    for(int i=0; word1[i]!=0; i++) H1[word1[i]-'a']++;
    for(int i=0; word2[i]!=0; i++) H2[word2[i]-'a']++;
    //先看「字母」是否有出現
    for(int i=0; i<26; i++){
        if((H1[i]>0&&H2[i]==0)||(H1[i]==0&&H2[i]>0)) return false;
        //一邊有出現、另一邊卻沒出現
    }
    qsort(H1, 26, sizeof(int), comp); //照出現次數排序
    qsort(H2, 26, sizeof(int), comp);
    for(int i=0; i<26; i++){ //出現次數不同，就失敗
        if(H1[i]!=H2[i]) return false;
    }
    return true;
}
