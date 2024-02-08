int countPrimes(int n) {
    if(n<2) return 0;
    int killed[n];
    memset(killed, 0, sizeof(int)*n);
    int ans = 0;
    for(int i=2; i<n; i++){
        if(killed[i]==0){
            ans++;
            for(int k=i+i; k<n; k+=i){
                killed[k] = 1;
            }
        }
    }
    return ans;
}
//case 17/66: n=499979
