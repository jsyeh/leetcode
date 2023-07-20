int maxProfit(int* prices, int pricesSize){
    int table[pricesSize+1]; //table[i] 之前的最低點
    table[0] = prices[0];

    int ans = 0;
    for(int i=1; i<pricesSize; i++){
        if(prices[i]-table[i-1]>ans) ans = prices[i]-table[i-1];
        table[i] = table[i-1];
        if(prices[i]<table[i]) table[i] = prices[i];
    }
    return ans;
}
