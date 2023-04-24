int squareAll(int n){
    int sum=0;
    while(n>0){
        sum += (n%10)*(n%10);
        n = n / 10;
    }
    return sum;
}
bool isHappy(int n){
    int n2 = n;
    while(n!=1){
        printf("%d ", n);
        n = squareAll(n);
        n2 = squareAll(squareAll(n2));
        if(n2!=1 && n==n2) return false;
    }
    return true;
}
