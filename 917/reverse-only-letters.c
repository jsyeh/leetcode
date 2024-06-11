char* reverseOnlyLetters(char* s) {
    char letter[100], N = 0;
    for(int i=0; s[i]!=0; i++){
        if(s[i]>='a' && s[i]<='z') letter[N++] = s[i];
        else if(s[i]>='A' && s[i]<='Z') letter[N++] = s[i];
    }
    for(int i=0; s[i]!=0; i++){
        if(s[i]>='a' && s[i]<='z') s[i] = letter[--N];
        else if(s[i]>='A' && s[i]<='Z') s[i] = letter[--N];
    }
    return s;
}
