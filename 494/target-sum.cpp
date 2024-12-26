// LeetCode 494. Target Sum
// nums[i] 前面可放「正號」或「負號」，希望湊出target結果，有幾種湊法。
// 不能直接暴力試 2^1000 種可能。但可用 Dynamic Programming 找結果
// 使用 Top-Down DP 的方法，函式呼叫函式，把問題解掉。
class Solution {
public:
    int helper(vector<int>& nums, int i, int total, int target, unordered_map<int,int>& map) {
        if(i==nums.size() && total==target) return 1;
        if(i==nums.size() && total!=target) return 0;
        auto key = i*10000+total; // 因total<=1000，不同 i 和 total 一定會做出不同的 key
        if(map.count(key) > 0) return map[key]; // 若 key 有出現過，則答案有算過，map[key] 直接拿來用
        int ans = helper(nums, i+1, total-nums[i], target, map);
        ans += helper(nums, i+1, total+nums[i], target, map);
        map[key] = ans; // 把答案記起來，方便下次使用
        return ans;
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        unordered_map<int,int> map; // Hash Map 方便記憶答案
        return helper(nums, 0, 0, target, map);
    }
};
