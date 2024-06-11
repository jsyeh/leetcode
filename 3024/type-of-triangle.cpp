// 三角形分成:正三角形equilateral、等腰三角isosceles, 其他scalene 
class Solution {
public:
    string triangleType(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if(nums[0]+nums[1]<=nums[2]) return "none";
        else if(nums[0]==nums[1] && nums[1]==nums[2]) return "equilateral";
        else if(nums[0]==nums[1] || nums[1]==nums[2]) return "isosceles";
        else if(nums[0]+nums[1]>nums[2]) return "scalene";
        else return "none";
    }
};
