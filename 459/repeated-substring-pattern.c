bool repeatedSubstringPattern(char * s){
    int N = strlen(s);
    char s2[N*2+1];
    strcpy(s2,s);
    strcat(s2,s);
    s2[N*2-1]='\0';
    char ans = strstr(s2+1, s);
    if(ans == NULL) return false;
    else return true;
}
