// LeetCode 2367. Number of Arithmetic Triplets
// 請問有幾組 i<j<k 使得 nums[i] nums[j] nums[k] 距離 diff
class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int ans = 0;
        for(int i=0; i<nums.size()-2; i++){
            for(int j=i+1; j<nums.size()-1; j++){
                for(int k=j+1;k<nums.size(); k++){
                    if(nums[j]-nums[i]==diff && nums[k]-nums[j]==diff){
                        ans++;
                    }
                }
            }
        }
        return ans;
    }
};
