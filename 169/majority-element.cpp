class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end()); //從小到大排好
        int ans = nums[0], ansCount = 1;

        int now = nums[0], nowCount = 1;
        for(int i=1; i<nums.size(); i++) {
            if(nums[i]==nums[i-1]) { //有重覆
                nowCount++;
            } else { //沒有重覆
                if(nowCount>ansCount) {
                    ansCount = nowCount;
                    ans = now;
                }
                now = nums[i];
                nowCount = 1;
            }
        }
        if(nowCount > ansCount){
            ans = now;
            ansCount = nowCount;
        }
        return ans;
    }
};
