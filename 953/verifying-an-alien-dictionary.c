int comp(char c1, char c2, char* order){
    if(c1==c2) return 0; //0:相等
    for(int i=0; i<26; i++){
        if(order[i]==c1) return -1; //左邊比較前面
        if(order[i]==c2) return +1; //右邊比較前面
    }
    return 0;
}
int compStr(char* s1, char* s2, char* order){
    int i=0;
    for(   ; s1[i]!=0 && s2[i]!=0; i++){
        int diff = comp(s1[i],s2[i], order);
        if(diff!=0) return diff;
    }
    if(s1[i]==0 && s2[i]==0) return 0;
    if(s1[i]==0) return -1;
    else return +1;

}
bool isAlienSorted(char ** words, int wordsSize, char * order){
    //先把字母翻譯好,再看是否有排序好
    //不對不對, 應該說, 要有個 qsort()的comp()函式, 能幫忙比大小
    for(int i=0; i<wordsSize-1; i++){
        if(compStr(words[i], words[i+1], order)>0) return false;
    }
    return true;
}
