class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        if(nums.size()==0) return ans;

        string line = "" + to_string(nums[0]);
        int a = nums[0], b;
        for(int i=1; i<=nums.size(); i++) {
            if(i!=nums.size() && nums[i-1]+1==nums[i])continue;
            else {
                if(a==nums[i-1]) ans.push_back(line);
                else {
                    line = line + "->" + to_string(nums[i-1]);
                    ans.push_back(line);
                }
                if(i!=nums.size()) {
                    a = nums[i];
                    line = ""+ to_string(nums[i]);
                }
            }
        }

        return ans;
    }
};
