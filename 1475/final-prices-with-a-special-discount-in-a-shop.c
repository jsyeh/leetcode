// LeetCode 1475. Final Prices With a Special Discount in a Shop
// prices[i] 特價規則：減掉「右邊第1個<=它」的數
int* finalPrices(int* prices, int pricesSize, int* returnSize) {
    for(int i=0; i<pricesSize; i++) {
        for(int j=i+1; j<pricesSize; j++) {
            if(prices[i]>=prices[j]) {
                prices[i] -= prices[j];
                break;
            }
        }
    }
    *returnSize = pricesSize;
    return prices;    
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

