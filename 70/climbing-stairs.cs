// 典型的 Dynamic Programming 題目：大問題可拆解、去問「小問題」
// 程式碼看起來也和 Fibonacci 數列很像
public class Solution {
    public int ClimbStairs(int n) {
        int [] a = new int[n+1];
        a[0] = 1;
        a[1] = 1;
        for(int i=2; i<=n; i++){
            a[i] = a[i-1] + a[i-2];
        } //每一步，都與前2格有關
        return a[n];
    }
}
