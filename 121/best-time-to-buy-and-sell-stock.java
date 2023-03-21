class Solution {
    public int maxProfit(int[] prices) {
        int lowest=prices[0];
        int ans = 0;
        for(int i=1; i<prices.length; i++) {
            if(prices[i]<lowest) lowest=prices[i];
            if(prices[i]-lowest>ans) ans = prices[i]-lowest;
        }
        return ans;
    }
    /*public int maxProfit(int[] prices) {
        //這不是好的寫法,因為太暴力、太浪費。
        //看了別人的 solution 我就照著 time machine 的方法重寫, 只要1個迴圈
        int ans = 0;
        int N = prices.length;
        for(int i=0; i<N; i++) {
            for(int j=i+1; j<N; j++){
                if(prices[j]-prices[i] > ans) ans = prices[j]-prices[i];
            }
        }
        return ans;
    }*/
}
