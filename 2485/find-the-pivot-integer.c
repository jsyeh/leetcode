//LeetCode 2485. Find the Pivot Integer
int pivotInteger(int n) {
    int total = 0;
    for(int i=1; i<=n; i++){
        total += i;
    }

    int left = 0;
    for(int i=1; i<=n; i++){
        left += i;
        if(left+left-i==total) return i;
    }
    return -1; //如果都沒有成功, 就-1
}
