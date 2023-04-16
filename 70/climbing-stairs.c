int climbStairs(int n){
    int a[50];
    a[0]=1;
    a[1]=1;
    for(int i=2; i<=n; i++){
        a[i] = a[i-1]+a[i-2];
    }
    return a[n];
}
