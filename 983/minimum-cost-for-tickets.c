// LeetCode 983. Minimum Cost For Tickets
// 坐火車有一日券、七日券、30日券，票價是 costs[0] cost2[1] costs[2]
// 不是每天都需要坐火車，days[i] 才要坐火車。問你怎麼買票「最便宜」
int table[366][366+30];
int min(int a, int b, int c) {
    if(a<=b && a<=c) return a;
    else if(b<=a && b<=c) return b;
    else return c;
}
int helper(int i, int passDay, int* days, int daysSize, int* costs, int costsSize) {
    if(i==daysSize) return 0;
    if(table[i][passDay] != -1) return table[i][passDay]; // 表格裡有「答案」，直接用答案

    if(days[i]<passDay) table[i][passDay] = helper(i+1, passDay, days, daysSize, costs, costsSize); // N日券夠用，繼續試
    else { // N日券「不夠用」，要再買
        int ans1 = helper(i+1, days[i]+1, days, daysSize, costs, costsSize) + costs[0]; // 買1日券試試
        int ans7 = helper(i+1, days[i]+7, days, daysSize, costs, costsSize) + costs[1]; // 買7日券試試
        int ans30 = helper(i+1, days[i]+30, days, daysSize, costs, costsSize) + costs[2]; // 買30日券試試
        table[i][passDay] = min(ans1, ans7, ans30); // 答案放入「表格」
    }
    return table[i][passDay]; // 表格裡有「答案」，直接用答案
}
int mincostTickets(int* days, int daysSize, int* costs, int costsSize) {
    for(int i=0; i<366; i++){
        for(int j=0; j<366+30; j++){
            table[i][j] = -1; // 表格清空
        }
    }
    return helper(0, 0, days, daysSize, costs, costsSize);
}
