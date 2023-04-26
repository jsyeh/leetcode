int getLucky(char * s, int k){
    int sum = 0;
    for(int i=0; s[i]!=0; i++){
        int now = s[i]-'a'+1;
printf("%d", now);
        sum += now%10;
        sum += now/10;
    }

    int n = sum;
    for(int i=0; i<k-1; i++){
printf("\n%d", n);
        sum = 0;
        while(n>0){
            sum += n%10;
            n = n / 10;
        }
        n = sum;
    }
    return n;
}
