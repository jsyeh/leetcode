class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int N = cost.length;
        int [] table = new int[N+1];
        table[0] = 0; //一開始可站在 index 0 免費
        table[1] = 0; //一開始可站在 index 1 免費
        for(int i=2; i<=N; i++){
            table[i] = Math.min( table[i-1]+cost[i-1], table[i-2]+cost[i-2]);
                     //如果踩在前一格的值+那格走1步的cost  踩在前2格的值+那格走2步的cost
        }
        return table[N];
    }
}//Case1: 10, 15, 20, _top_
//table[]  0   0  ......
