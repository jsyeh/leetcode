int mySqrt(int x){
    if(x==0) return 0;

    //可以用binary search 慢慢去逼近答案。
    //不過因為 ans*ans 超過 32bit 就會爛掉
    //(1) 可以給 32bit 最適合的初始值, 剛好不會爆掉
    //(2) 用 long long int 來解決問題
    
    long long int left = 0, right = x;
    while(left<right){
        long long int mid = (left+right)/2;
    //printf("mid:%lld mid*mid:%lld\n", mid, mid*mid);
        if(mid*mid==x) return mid;
        if(mid*mid<x){
            left = mid+1;
        }else{
            right = mid;
        }
    }
    //printf("left:%lld\n", left);

    if(left*left<=x) return left;
    else return left - 1;
}
