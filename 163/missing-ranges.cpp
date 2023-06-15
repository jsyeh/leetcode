class Solution {
public:
    vector<vector<int>> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<vector<int>>ans;
        if(nums.size()==0) {
            vector<int> list;
            list.push_back(lower);
            list.push_back(upper);
            ans.push_back(list);
            return ans;
        }

        int prev = lower-1;
        for(int i=0; i<nums.size(); i++) {
            if(prev+1!=nums[i]){
                vector<int> list;
                list.push_back(prev+1);
                list.push_back(nums[i]-1);
                ans.push_back(list);
            }
            prev = nums[i];
        }
        if(prev!=upper) {
            vector<int> list;
            list.push_back(prev+1);
            list.push_back(upper);
            ans.push_back(list);
        }
        return ans;
    }
};
