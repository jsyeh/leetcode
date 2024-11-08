// LeetCode 2275. Largest Combination With Bitwise AND Greater Than Zero
class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int ans = 0;
        for(int i=0; i<24; i++) { // 針對每個 bit 可能的位置
            int bit = 1 << i; // 製作出對應的 bit
            int count = 0;
            for(int now : candidates) { // 針對每個數字，比對「對應 bit」
                if((now & bit) > 0) count++; // 如果有對應 bit，就多投1票
            }
            ans = max(ans, count);
        }
        return ans;
    }
};
