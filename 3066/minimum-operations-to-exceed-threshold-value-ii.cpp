// LeetCode 3066. Minimum Operations to Exceed Threshold Value II
// nums 每次挑最小的2個數x,y去除，再於任意處加入 min(x,y)*2+max(x,y)
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        priority_queue<long long> heap; // 建出 priority_queue 資料結構，想找最小值
        for(long long num : nums) heap.push(-num); // 但它會吐出「最大值」，所以「加負號」
        int ans = 0; // 要做幾次，才能將 nums 裡，全部的數都 >= k 呢？
        while(heap.size()>0 && heap.top() > -k) { // heap 還有值，且「值不符合需求」
            long long x = heap.top();
            heap.pop(); // 吐出2個最小的數
            long long y = heap.top();
            heap.pop();
            heap.push(x+y+max(x,y)); // 負的數，要倒過來
            ans++;
        }
        return ans;
    }
};
