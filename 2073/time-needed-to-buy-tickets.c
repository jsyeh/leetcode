// LeetCode 2073. Time Needed to Buy Tickets
// 今天的題目很簡單, 每個人要買的票數量不同, 每次只能買一張票, 依序買
// 問第k個人要多久時間, 才能買完他想要的 tickets[k] 個票。
// 技巧: 「排在他前面的人」最多要一樣多的票, 最少就是「要多少買多少」
// 「排在他後面的人」最多要買 tickets[k]-1張票, 最少就是「要多少買多少」
int timeRequiredToBuy(int* tickets, int ticketsSize, int k) {
    int ans = 0;
    for(int i=0; i<=k; i++){ //排在他前面的人, 包含本人
        if(tickets[i]<=tickets[k]) ans += tickets[i];//「要多少買多少」
        else ans += tickets[k]; //一樣多張票
    }
    for(int i=k+1; i<ticketsSize; i++){ //排在他後面的人, 
        if(tickets[i]<tickets[k]) ans += tickets[i];//「要多少買多少」
        else ans += tickets[k]-1; //少1張
    }
    return ans;
}
