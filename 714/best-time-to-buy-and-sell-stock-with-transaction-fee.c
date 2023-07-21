int maxProfit(int* prices, int pricesSize, int fee){
    int N = pricesSize;
    int table[N]; //如果 day i 早已賣出時，可賺到 table[i] 最多錢
    int hold[N]; //如果 day i 這時候持有商品 hold[i] 就是它的最低成本 (最接近0的負數)
    for(int i=0; i<N; i++){
        table[i] = 0;
        hold[i] = 0;
    }

    hold[0] = -prices[0]; //一開始買，所以資產為負數
    table[0] = 0; //手上沒東西，賺到的錢是0
    for(int i=1; i<N; i++){
        //下面是「現在手上空空」時，賺的錢
        table[i] = table[i-1]; //可能是之前就膁的錢
        int profit = prices[i] + hold[i-1] - fee; //如果今天賣，能賺這麼多
        if(profit>table[i]) table[i] = profit; //能賺更多錢，更新

        //下面是另一個表格，解釋 day i (還持有時)賺的錢
        hold[i] = hold[i-1]; //可能是之前就賺的錢
        profit = table[i-1] - prices[i]; //也可能是之前
        if(profit>hold[i]) hold[i] = profit;
    }
    return table[N-1];
}
