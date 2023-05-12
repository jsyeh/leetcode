class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>>ans;
        vector<int>list;
        vector<bool>used(nums.size(), false);
        bruteforce(nums, used, 0, list, ans);
        return ans;
    }
    void bruteforce(vector<int>& nums, vector<bool>& used, int usedN, vector<int> list, vector<vector<int>>& ans) {
        if(usedN==nums.size()){
            ans.push_back(list);
            return;
        }
        for(int i=0; i<nums.size(); i++) {
            if(!used[i]){
                used[i]=true;
                list.push_back(nums[i]);
                bruteforce(nums, used, usedN+1, list, ans);
                list.pop_back();
                used[i]=false;
            }
        }
    }
};
