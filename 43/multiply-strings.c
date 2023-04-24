char * multiply(char * num1, char * num2){
    int N1 = strlen(num1);
    int N2 = strlen(num2);

    int * ans = (int*)malloc((N1+N2+2)*sizeof(int));

    if(num1[0]=='0' || num2[0]=='0'){
        char * string = (char*) malloc(2);
        string[0] = '0';
        string[1] = 0;
        return string;
    }

    for(int i=0; i<N1+N2+2; i++) ans[i] = 0;
    
    int len=0;
    for(int i=0; i<N1; i++) {
        int a = num1[N1-1-i]-'0';
        int carry=0;
        for(int j=0; j<N2; j++){
            int b = num2[N2-1-j]-'0';
            int now = a*b + carry + ans[i+j];
            ans[i+j] = now%10;
            carry = now/10;
        }
        len = i+N2;
        ans[i+N2] = carry%10;
        ans[i+N2+1] = carry/10;
        if(carry/10>0) {
            len += 2;
        }else if(carry%10>0) {
            len += 1;
        }
        //for(int k=0; k<N1+N2+1; k++) printf("%d ", ans[k]);
        //printf("\n");
    }
    char * string = (char*) malloc(N1+N2+2);
    for(int i=0; i<len; i++){
        string[i] = ans[len-1-i]+'0';
    }
    string[len]=0;
    return string;
}//case 302/311: "9133" "0"
