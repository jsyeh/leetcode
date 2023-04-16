class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans;
        ans.push_back(1);
        for(int level=1; level<=rowIndex; level++) {
            ans.push_back(1);
            for(int i=ans.size()-2; i>=1; i--) {
                ans[i] = ans[i] +ans[i-1];
            }
        }
        return ans;
    }
};
