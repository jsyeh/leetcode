// LeetCode 2779. Maximum Beauty of an Array After Applying Operation
// nums[i] 的每個數，能「上下調整k格」，問最多能調出幾個「相同的數」
// 這裡用的解法，是我在 Solutions 裡，隨手翻到的 Khosiyat 寫的解法。
// 想像「每個數」若「上下調整k格」會產生 nums[i]+k 和 nums[i]-k 兩個界限
// 把上下邊界+對應的+1或-1變化，整個拿去排序，再巡一次，便能知「在範圍內數目的變化」
class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        int N = nums.size(); // 先知道有 N 個數
        vector<vector<int>> bound(N*2); // 做出 N*2 個小邊界
        for(int i=0; i<nums.size(); i++){
             // 因 sort()是小到大，先左邊、再右邊數，所以把右邊正負倒過來
            vector<int> now {nums[i]-k, -1};
            bound[i*2] = now;
            vector<int> now2 {nums[i]+k, +1};
            bound[i*2+1] = now2;
        }
        sort(bound.begin(), bound.end());
        int ans = 0, inRange = 0; // 現在有幾個數在這個邊界裡
        for(auto now : bound){
            inRange -= now[1]; // 因 now[1] 正負倒過來，所以再倒過來一次
            ans = max(ans, inRange); // 更新答案
        }
        return ans;
    }
};
