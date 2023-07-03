class Solution {
public:
    int rob(vector<int>& nums) {
        int N = nums.size();
        if(N==1) return nums[0];
        if(N==2) return max(nums[0], nums[1]);
        int a[N], b[N];
        a[0] = 0; //因為一定不搶 nums[0] //a[0] = nums[0];
        a[1] = nums[1];
        a[2] = nums[2];

        b[0] = nums[0];//b一定要搶 nums[0]
        b[1] = 0; //因為一定要搶 nums[1] 所以
        b[2] = nums[2] + nums[0];
        for(int i=3; i<N; i++) {
            a[i] = nums[i] + max(a[i-2], a[i-3]);
            b[i] = nums[i] + max(b[i-2], b[i-3]);
printf("a[i]:%d b[i]%d\n", a[i], b[i]);
        }
        //前面都和 LeetCode 198. House Robber 一樣
        //不過不知道到底 a[0] 有沒有被用到，所以應該要有 2個陣列分別存
        //int ans = max(a[N-1], b[N-2]);
        int ans1 = max(a[N-1], a[N-2]);
        int ans2 = max(b[N-2], b[N-3]);
        return max(ans1, ans2);
        // a[N-1] 是不搶 nums[0] 但要搶 nums[N-1]
        // b[N-2] 是要搶 nums[0] 且不搶 nums[N-1]
    }
};
