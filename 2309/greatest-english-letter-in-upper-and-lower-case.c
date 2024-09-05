// LeetCode 2309. Greatest English Letter in Upper and Lower Case
// 「同時有大寫、小寫」的字母，找到最大的。
char ans[2] = {}; //還沒有答案
char* greatestLetter(char* s) {
    int Upper[26]={}, Lower[26]={}; //都還沒出現過，都0
    for(int i=0; s[i]!=0; i++){
        if(isupper(s[i])) Upper[s[i]-'A']++;
        else Lower[s[i]-'a']++;
    }
    for(int i=25; i>=0; i--){
        if(Upper[i]>0 && Lower[i]>0){ //大小寫都有出現過
            ans[0] = 'A'+i;
            ans[1] = 0;
            return ans;
        }
    }
    ans[0] = 0; // 沒有找到答案
    return ans;
}
