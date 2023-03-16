class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        std::sort(nums.begin(), nums.end() );
        int N = nums.size();
        int prevI = -999999;
        for(int i=0; i<N; i++){
            if(nums[i]==prevI) continue;
            else prevI = nums[i];

            int prevJ = -999999;
            for(int j=i+1; j<N; j++){
                if(nums[j]==prevJ) continue;
                else prevJ = nums[j];

                //第3個部分,應該用binary search找出對應的值
                int val = -(nums[i]+nums[j]);
                if (std::binary_search (nums.begin()+j+1, nums.end(), val)){
                    vector<int> now;
                    now.push_back(nums[i]);
                    now.push_back(nums[j]);
                    now.push_back(val);
                    ans.push_back(now);
                }
            }
        }
        return ans;
    }
};
