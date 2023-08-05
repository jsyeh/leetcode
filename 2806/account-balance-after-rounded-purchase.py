class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        int ans=100-purchaseAmount;
        ans +=4;
        ans /= 10;
        ans *= 10;
            
        return ans;
    }
}
