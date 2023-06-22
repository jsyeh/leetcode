//這題的解決方案，是看 Editorial 裡的解法，分成兩個表格來更新
class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int [] table1 = new int[n];//目前持有的-最低成本（買）
        //可能之前就買了
        int [] table2 = new int[n];//目前沒有持有的最高獲利（賣）
        //可能是之前就賣了
        
        table1[0] = -prices[0]; //一開始買，的確就持有了，口袋的錢變負的
        table2[0] = 0;//手上空空時，也沒有任何獲利
        for(int i=1; i<n; i++){
            table1[i] = table1[i-1]; //本來就有的持有成本
            if(table2[i-1] - prices[i] > table1[i]) { //若新持有的成本更低
                table1[i] = table2[i-1] - prices[i];
            } //之前已賣出，現在買，相對的現金變更多的話，就從「無」到「有」買

            table2[i] = table2[i-1]; //之前兩手空空時的最高獲利
            if(table1[i-1] + prices[i] - fee > table2[i]) { //手上賣掉（扣手續費）有更高的獲利
                table2[i] = table1[i-1] + prices[i] - fee;
            }
        }


        return table2[n-1];//查看目前的最佳獲利狀況
    }
}
