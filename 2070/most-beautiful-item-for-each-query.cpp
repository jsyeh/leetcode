// LeetCode 2070. Most Beautiful Item for Each Query
// 每個 items 裡有 price 和 beauty 的值
// 每次 query 時，要找到 price < queries[i] 的最 beauty 的值
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        sort(items.begin(), items.end()); // 先照著 price 小到大排好
        int beauty = 0;
        int N = items.size();
        vector<int> prices(N);
        vector<int> beauties(N);
        for(int i=0; i<N; i++) {
            if(beauty>items[i][1]) items[i][1] = beauty; // 更新 item[1] 存「目前最beauty值」
            else beauty = items[i][1]; // 更 beauty 的 item[1] 來更新 beauty
            prices[i] = items[i][0]; // 再把答案，放入兩個分開的陣列
            beauties[i] = items[i][1]; // 再把答案，放入兩個分開的陣列
        }
        vector<int> ans(queries.size()); // 照 queries 的長度，準備 ans 的格子數
        for(int i=0; i<queries.size(); i++) { // 逐一找答案
            auto pos = upper_bound(prices.begin(), prices.end(), queries[i]);
            if(pos==prices.begin()) ans[i] = 0; // 如果插入點在最前面，表示左邊沒有值，答案是0
            else ans[i] = beauties[pos - prices.begin() -1]; // 左邊有值，把左邊那個值對應的beauty值取出
        }
        return ans;
    }
};
