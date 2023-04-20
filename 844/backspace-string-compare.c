bool backspaceCompare(char * s, char * t){
    char a1[203], a2[203];
    int N1=0, N2=0;

    while(*s!=0){
        if(*s=='#'){
            if(N1>0)  N1--;
        }else{
            a1[N1]=*s;
            N1++;
        }
        s++;
    }

    while(*t!=0){
        if(*t=='#'){
            if(N2>0) N2--;
        }else{
            a2[N2]=*t;
            N2++;
        }
        t++;
    }
    if(N1!=N2) return false;
    for(int i=0; i<N1; i++){
        if(a1[i]!=a2[i]) return false;
    }
    return true;
}
