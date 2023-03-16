class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        int N = nums.size();

        int prevI=-2000000000;
        for(int i=0; i<N; i++){
            if(prevI==nums[i]) continue;
            else prevI=nums[i];
            
            int prevJ=-2000000000;
            for(int j=i+1; j<N; j++){
                if(prevJ==nums[j]) continue;
                else prevJ=nums[j];

                int prevK=-2000000000;
                for(int k=j+1; k<N; k++){
                    if(prevK==nums[k]) continue;
                    else prevK=nums[k];

                    long long int val = 0;
                    val += target;
                    val -= nums[i];
                    val -= nums[j];
                    val -= nums[k];
                    if(val<INT_MIN || val>INT_MAX) continue;

                    if(binary_search(nums.begin()+k+1, nums.end(), val)){
                        vector<int> now;
                        now.push_back(nums[i]);
                        now.push_back(nums[j]);
                        now.push_back(nums[k]);
                        now.push_back(val);
                        ans.push_back(now);
                    }
                }
            }
        }
        return ans;
    }
};
