// LeetCode 539. Minimum Time Difference
// 給一堆字串，內含 24小時制的時間，問「它們間最小的時間差多少?」
class Solution {
public:
    int timePoint2int(string t){ // 手動將字串變成時間的分鐘數
        return (t[0]-'0')*600 + (t[1]-'0')*60 + (t[3]-'0')*10 + (t[4]-'0');
    }
    int findMinDifference(vector<string>& timePoints) {
        sort(timePoints.begin(), timePoints.end()); // 先字串排序
        int ans = INT_MAX;
        int ii = timePoints.size() - 1;
        int prev = timePoint2int(timePoints[ii]) - 24*60; //跨午夜，變成前一筆
        for(int i=0; i<timePoints.size(); i++){ // now 與 prev 比較
            int now = timePoint2int(timePoints[i]);
            if(now-prev < ans) ans = now-prev;
            prev = now;
        }
        return ans;
    }
};
