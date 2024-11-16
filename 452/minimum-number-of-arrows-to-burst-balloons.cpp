// LeetCode 452. Minimum Number of Arrows to Burst Balloons
// 氣球黏在牆上排一排，每個氣球超寬，射箭時，只要在 [start,end]碰到，就會破
// 最多有10萬個氣球，要將全部氣球射破，最少要射幾枝箭？
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end()); // 以 begin 為主，小到大排好
        int N = points.size();
        int ans = 1, prevShot = points[N-1][0]; // 第1箭，射在最後1個左界
        for(int i=N-2; i>=0; i--) { // 接下來，倒著巡其他筆
            if(points[i][1]<prevShot){ // 如果「前一箭」沒能射到
                prevShot = points[i][0]; // 就射此氣球的左界
                ans++; // 多了一箭
            }
        }
        return ans;
    }
};
