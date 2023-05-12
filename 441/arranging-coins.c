long long int triangle(long long int n){
    return (1+n)*n/2;
}
int arrangeCoins(int n){
    //答案需要 triangle(ans)<=n && n<triangle(ans+1)
    long long int left=1, right=n;
    while(left<right){
        //printf("%d %d\n", left, right);
        long long int mid = (left+right)/2;
        if(triangle(mid)<=n && n<triangle(mid+1)) {printf("mid:%d\n", mid); return mid;}
        if(triangle(mid)<n){
            left=mid+1;
        }else right=mid;
    }
    //printf("Final: %d %d\n", left, right);
    return (int)left;
}
//case 12/1335: 1804289383
