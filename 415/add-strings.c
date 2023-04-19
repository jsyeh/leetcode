char * addStrings(char * num1, char * num2){
    int N1 = strlen(num1), N2 = strlen(num2);
    char * str = (char*)malloc(10002);
    int revAns[10002], N=0;

    int carry=0;
    for(int i=0; i<10001; i++){
        int i1=N1-1-i, i2=N2-1-i;
        int now = carry;
        
        if(i<N1) now += num1[i1]-'0';
        if(i<N2) now += num2[i2]-'0';
        if(now>=10){
            carry = 1;
            now %= 10;
        }else carry=0;
        revAns[i] = now;
        if(now==0 && carry==0 && i>=N1 && i>=N2){
            N = i;
            break;
        }
    }
    for(int i=0; i<N; i++){
        str[i]=revAns[N-1-i]+'0';
    }
    str[N]=0;
    return str;
}//case 211/317: "6" "501"
