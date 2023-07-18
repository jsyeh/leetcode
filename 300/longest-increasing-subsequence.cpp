class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int N = nums.size();
        int table[N]; //table[i] 表示包含 nums[i] 的 LIS 長度
        table[0] = 1;
        int ans = 1;
        for(int i=1; i<N; i++){
            int maxLIS = 1; //自己本身孤單時，也有LIS為1
            for(int k=0; k<i; k++){
                if(nums[k]<nums[i]){
                    if(table[k]+1>maxLIS) maxLIS = table[k]+1;
                }
            }
            table[i] = maxLIS;
            if(maxLIS>ans) ans = maxLIS;
        }
        return ans;
    }
};
