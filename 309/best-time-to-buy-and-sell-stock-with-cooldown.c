//這題在DP時，要倒過來處理
//這題我本來沒什麼頭緒，不過看了 Editorial 的解釋後，覺得想法和 Approach 2 有點像
int maxProfit(int* prices, int pricesSize){
    int N = pricesSize;
    int table[N+2]; //table[i] 表示在買在day i 的最終獲利, +2是為了賣及cooldown的格子
    for(int i=0; i<=N+1; i++) table[i] = 0; //預設沒賺到錢
    //table[N+1] 是最右邊的狀況，
    //供 day N-1賣，day N 冷靜，要查 table[k+2]時用的 day N+1

    for(int i=N-1; i>=0; i--){ //倒過來處理
        table[i] = table[i+1]; //假設不要買在這天，就查 day i+1 的答案

        //買在 day i, buy, sell, cooldown
        for(int k=i+1; k<N; k++){ //暴力去試各種切法，要賣在哪一天？
            //賣在 day k
            int profit = (prices[k] - prices[i]) + table[k+2]; 
            //table[k+2] 是因為：賣及cooldown，下次有機會買是在 k+2
            if(profit>table[i]) table[i] = profit;
        }
    }
    return table[0];
}
