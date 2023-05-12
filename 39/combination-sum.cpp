class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>>ans;
        vector<int> list;
        bruteforce(candidates, target, 0, list, ans);
        return ans;
    }
    void bruteforce(vector<int>& candidates, int target, int now, vector<int>list, vector<vector<int>>& ans) {
        for(int i=now; i<candidates.size(); i++) {
            if(candidates[i]>target) break;
            if(candidates[i]==target) {
                list.push_back(candidates[i]);
                ans.push_back(list);
                list.pop_back();
            }
            if(candidates[i]<target) {
                list.push_back(candidates[i]);
                bruteforce(candidates, target-candidates[i], i, list, ans);
                list.pop_back();
            }
        }
    }
};
