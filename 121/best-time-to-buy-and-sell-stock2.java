class Solution {
    public int maxProfit(int[] prices) {
        int minBuy = prices[0], maxProfit = 0;
        for(int i=0; i<prices.length; i++) {
            if(prices[i]-minBuy>maxProfit) maxProfit = prices[i]-minBuy;
            if(prices[i]<minBuy) minBuy = prices[i];
        }
        return maxProfit;
    }
}
