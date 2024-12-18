// LeetCode 1475. Final Prices With a Special Discount in a Shop
// prices[i] 特價規則：減掉「右邊第1個<=它」的數
class Solution {
    public int[] finalPrices(int[] prices) {
        for(int i=0; i<prices.length; i++) {
            for(int j=i+1; j<prices.length; j++) {
                if(prices[i]>=prices[j]) {
                    prices[i] -= prices[j];
                    break;
                }
            }
        }
        return prices;        
    }
}
