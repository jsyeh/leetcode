// LeetCode 862. Shortest Subarray with Sum at Least K
// 在 nums 裡，找一段「最短的連續subarray」，加起來>=k。
// 但裡面有正、有負，不能用直覺的 sliding window 毛毛蟲法。要用 Mono Queue 來解
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        deque<pair<int,long long>> queue;
        queue.push_back(pair(-1,0));
        long long int ans = LLONG_MAX, total = 0;
        for(int i=0; i<nums.size(); i++) {
            total += nums[i];
            while(queue.size()>0 && total - queue[0].second >= k) {
                if(i-queue.front().first < ans) ans = i - queue.front().first;
                queue.pop_front();
            }
            while(queue.size()>0 && total <= queue[queue.size()-1].second) {
                queue.pop_back();
            }
            queue.push_back(pair(i,total));
        }
        if(ans==LLONG_MAX) return -1;
        return ans;
    }
};

