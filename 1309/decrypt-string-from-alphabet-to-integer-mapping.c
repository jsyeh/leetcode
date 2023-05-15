bool isDigit(char c){
    if(c>='0' && c<='9') return true;
    else return false;
}
char * freqAlphabets(char * s){
    int N = 0;
    for(int i=0; s[i]!=0; i++){
        if(isDigit(s[i]) && s[i+1]==0){ //字串結尾,送出1位的字母
            s[N++] = s[i]-'1'+'a';
//printf("(1)\n");
        }else if(isDigit(s[i]) && s[i+2]=='#'){
            s[N++] = (s[i]-'0')*10 + s[i+1]-'0' - 10 + 'j';
            i+=2;
//printf("(2)\n");
        }else{
            s[N++] = s[i]-'1'+'a';
//printf("(3)\n");
        }
//printf("%c", s[N-1]);
    }
    s[N] = 0;
    return s;
}
