// LeetCode 2054. Two Best Non-Overlapping Events
// events[i] 裡有 [startTime, endTime, value] 3 個值，挑「兩個事件」參加，value相加「最有價值」。但「兩個事件」不能重疊
class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end()); // Hint 1 建議照事件的 startTime 排序
        priority_queue<vector<int>> heap; // 照 事件的 endTime 排好，便能取出「不重疊」的舊事件
        // 但因 C++ priority_queue 在取出時，依序「大到小」，所以加「負號」便能反過來「小到大」取出
        int ans = 0; // ans是「兩個事件」 加起來的最大值
        int maxPrevVal = 0; // 「目前時間」之前的「舊事件」value最大值
        for(vector<int>& event : events) { // 照「開始時間」逐一考慮「新事件」
            int start = event[0], end = event[1], val = event[2];
            while(heap.size()>0 && -heap.top()[0] < start) { // 舊事件 與新事件不重疊（頭尾不相碰）
                maxPrevVal = max(maxPrevVal, heap.top()[1]); // 取出 heap 裡不重疊的事件，更新 maxPrevValue
                heap.pop(); // 在迴圈裡，便能更新之前不重疊的「舊事件」最大值
            }
            ans = max(ans, maxPrevVal + val); // 「舊事件」+「新事件」，更新「兩個事件」的價值
            vector<int> now {-end, val}; // 加「負號」便能反過來「小到大」取出
            heap.push(now); // 現在的「事件」也塞入 heap 變「舊事件」
        }
        return ans;
    }
};
