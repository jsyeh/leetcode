class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int N = nums.size(); //先知道陣列大小
        vector<int> ans(N); //準備好一樣大小的ans

        ans[0] = nums[0];
        for(int i=1; i<N; i++){
            ans[i] = ans[i-1] + nums[i];
        }

        return ans;
    }
};
