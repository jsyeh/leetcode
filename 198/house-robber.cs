// 典型的DP問題
public class Solution {
    public int Rob(int[] nums) {
        int N = nums.Length;
        if(N==1) return nums[0]; // 只有1家能偷
        if(N==2) return Math.Max(nums[0], nums[1]); //有2家能偷
        //以上是簡單的邊界狀況。下面則確認至少有3間房

        int [] table = new int[N];
        // table[i] 最後有偷 house[i] 的最多錢
        table[0] = nums[0];
        table[1] = nums[1];
        table[2] = nums[2]+nums[0];
        for(int i=3; i<N; i++){
            table[i] = nums[i] + Math.Max(table[i-2], table[i-3]);
        }
        // 不能偷「兩個連續房子」答案是 max(table[N-2], table[N-1])
        return Math.Max(table[N-1], table[N-2]);
    }
}
