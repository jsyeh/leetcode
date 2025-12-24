// LeetCode 3074. Apple Redistribution into Boxes
// 把 Apple 裝箱, 最少要幾箱? (大小箱子容量不同)
class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int total = 0;
        for (int i=0; i<apple.size(); i++) {
            total += apple[i]; // 先把 Apple 全部加起來
        }

        sort(capacity.begin(), capacity.end() ); // 把箱子小到大排好
        int ans = 0;
        for (int i=capacity.size()-1; i>=0; i--) {
            ans ++; // 要多用一個箱子
            total -= capacity[i]; // 全部裝到箱子裡
            if (total <= 0) break; // 裝光光、離開迴圈
        }
        return ans;
    }
};
