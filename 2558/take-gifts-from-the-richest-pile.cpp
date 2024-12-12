// LeetCode 2558. Take Gifts From the Richest Pile
// 從最多禮物的那堆，留下「開根號後」的禮物數量
class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> heap; // 要找「最大堆的禮物」可用 priority queue
        for(int gift : gifts) heap.push(gift); // 把 gift 轉成 priority queue

        for(int i=0; i<k; i++) { // 模擬「做k次」取禮物
            int now = heap.top(); // 最大堆的禮物
            heap.pop(); // 拿走
            heap.push(sqrt(now)); // 放回「開根號後」的禮物數量
        }

        long long int ans = 0; // 最後統計「剩下的禮物」
        while(heap.size()>0) { // 把 heap 逐一取出、慢慢清空
            ans += heap.top(); // 更新答案
            heap.pop(); // 把 heap 逐一取出、慢慢清空
        }
        return ans;
    }
};
