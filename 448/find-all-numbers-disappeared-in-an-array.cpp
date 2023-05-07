class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int N = nums.size();
        int appear[N+1];
        for(int i=1; i<=N; i++) appear[i] = 0;
        for(int i=0; i<N; i++){
            int n = nums[i];
            appear[n]++;
        }

        vector<int> ans;
        for(int i=1; i<=N; i++){
            if(appear[i]==0) ans.push_back(i);
        }
        return ans;
    }
};
