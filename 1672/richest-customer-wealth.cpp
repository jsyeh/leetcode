class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int ans = 0;
        for(int i=0; i<accounts.size(); i++){
            int total = 0;
            for(int j=0; j<accounts[i].size(); j++){
                total += accounts[i][j];
            }
            if(total>ans) ans = total;
        }
        return ans;
    }
};
