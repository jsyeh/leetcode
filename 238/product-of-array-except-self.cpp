class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int N = nums.size();
        vector<int> ans(N);
        //發現一個規律: 如果有1個0,那只有它有值。如果有2個0,那全部都是0
        int zeroN = 0;
        for(int i=0; i<N; i++){
            if(nums[i]==0) zeroN++;
        }
        if(zeroN>=2){
            for(int i=0; i<N; i++) ans[i] = 0;
            return ans;
        }
        if(zeroN==1){
            int all = 1, I=0;
            for(int i=0; i<N; i++){
                ans[i] = 0;
                if(nums[i]==0) I = i;
                else all *= nums[i];
            }
            ans[I] = all;
            return ans;
        }

        ans[0] = 1;
        for(int i=1; i<N; i++) {
            ans[0] *= nums[i];
        }

        for(int i=1; i<N; i++){
            ans[i] = ans[i-1] * nums[i-1] / nums[i];
        }
        return ans;
    }
};
