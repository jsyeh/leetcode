class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int N = nums.size();
        int left = 0, right = N;
        while(left<right){
            int mid = (left+right)/2;
            if(nums[mid]<target){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left;
    }
};
