int lengthOfLastWord(char * s){
    int len = 0, lastLen = 0;
    for(int i=0; s[i]!=0; i++){
        if(s[i]==' '){
            len = 0;
        }else{
            len++;
            lastLen = len;
        }
    }
    return lastLen;
}
