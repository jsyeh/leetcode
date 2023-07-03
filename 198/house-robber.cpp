class Solution {
public:
    int rob(vector<int>& nums) {
        int N = nums.size();
        if(N==1) return nums[0];
        if(N==2) return max(nums[0], nums[1]);
        int table[N+3]; //table[i] 表示要搶第i間房 的最多錢的狀況
        table[0] = nums[0];
        table[1] = nums[1];
        table[2] = nums[2] + nums[0];
        for(int i=3; i<N; i++){
            table[i] = nums[i] + max(table[i-2], table[i-3]);
        }
        int ans = table[N-1];
        if(N>2 && table[N-2]>ans) ans = table[N-2];
        //if(N>3 && table[N-3]>ans) ans = table[N-3];
        return ans;
    }
};
//case 2/27: [0]
//另外要試 [1,2] 及 [1,400,2]
