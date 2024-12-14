// LeetCode 57. Insert Interval
// 原本 intervals 插入 newInterval 後，合併重疊的部分，得到新答案
// 將「新插入」的 newinterval 把「原本的」intervals 合併「重疊」部分
// intervals vs. s2,e2 的3種狀況「都在前」「都在後」「交錯」
// 再看 StefanPochmann 的 Solution 2 想法是類似的，就寫吧
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int s2 = newInterval[0], e2 = newInterval[1]; // 要插入的 start, end 時間
        vector<vector<int>> left;
        vector<vector<int>> right;
        // 要處理的狀況有幾種：s2,e2都在前面、交錯、都在後面
        for (auto interval : intervals) {
            int start = interval[0], end = interval[1];
            if (end<s2) { // 在之前
                left.push_back( vector<int>{start,end}); // 「左邊國」
            } else if (e2<start) { // 在之後
                right.push_back( vector<int>{start, end}); // 「右邊國」
            } else { // 最難處理的交錯，就是要合併，將s2,e2放大
                s2 = min(start, s2); // 合併的新起點（偏左）
                e2 = max(end, e2); // 合併的新終點
            }
        }
        left.push_back(vector<int>{s2,e2}); // 「中間國」
        for(auto now : right) left.push_back(now); // 把「右邊國」塞入「左邊國」
        return left;
    }
};
