// LeetCode 2571. Minimum Operations to Reduce an Integer to 0
// 目標：把n變成0，每次可把數字「加減」2的i次方。像 1,2,4,8,16,32,...
// 看到 lee215 的解說，可用 bit 來想：最低1個1的話，就消掉。很多1個的話，就+1大量進位。
int minOperations(int n) {
    int ans = 0;
    while(n>0) {
        if(n%4==1) {
            n--;
            ans++;
        } else if(n%2==1) {
            n++;
            ans++;
        } else if(n%2==0) {
            n /= 2;
        }
    }
    return ans;
}
