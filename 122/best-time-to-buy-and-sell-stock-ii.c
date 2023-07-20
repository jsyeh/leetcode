int maxProfit(int* prices, int pricesSize){
    int ans = 0;
    int prevLow = prices[0];
    for(int i=1; i<pricesSize; i++){
        if(prices[i]>prevLow){
            ans += prices[i] - prevLow;
            prevLow = prices[i];
        }else if(prices[i]<prevLow){
            prevLow = prices[i];
        }
    }
    return ans;
}
