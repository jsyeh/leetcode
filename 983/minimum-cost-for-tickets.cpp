// LeetCode 983. Minimum Cost For Tickets
// 坐火車有一日券、七日券、30日券，票價是 costs[0] cost2[1] costs[2]
// 不是每天都需要坐火車，days[i] 才要坐火車。問你怎麼買票「最便宜」
class Solution {
public:
    int helper(int i, int passDay, int table[366][366+30], vector<int>& days, vector<int>& costs) {
        if(i==days.size()) return 0;
        if(table[i][passDay] != 0) return table[i][passDay]; // 若表格內有資料
        if(days[i]<passDay) {
            table[i][passDay] = helper(i+1, passDay, table, days, costs); // 放入表格
            return table[i][passDay];
        }
        int ans1 = helper(i+1, days[i]+1, table, days, costs) + costs[0]; // 一日券
        int ans7 = helper(i+1, days[i]+7, table, days, costs) + costs[1]; // 七日券
        int ans30 = helper(i+1, days[i]+30, table, days, costs) + costs[2]; // 30日券
        table[i][passDay] = min({ans1, ans7, ans30}); // 找最小值，放入表格
        return table[i][passDay];
    }
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int table[366][366+30] = {}; // 動態規劃的表格
        return helper(0, 0, table, days, costs);
    }
};
