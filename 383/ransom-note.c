bool canConstruct(char * ransomNote, char * magazine){
    int H[26] = {}; //Histogram of characters
    for(int i=0; magazine[i]!=0; i++){
        int c = magazine[i] - 'a';
        H[c]++;
    }
    for(int i=0; ransomNote[i]!=0; i++){
        int c = ransomNote[i] - 'a';
        if(H[c]>0) H[c]--;
        else return false; //無法找到需要的字母，就失敗
    }
    return true; //順利完成 ransomNote, 成功
}
