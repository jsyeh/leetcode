class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int left=0, right=0, ans=0, product=1;
        for(  ;left<nums.size(); left++) {
            //左邊界往右移,想查探對應右邊界
            while(right<nums.size() && product*nums[right]<k) { 
                //還可貪心繼續右移右邊界
                product *= nums[right++];
                //printf("product:%d\n", product);
            }
            //決定右邊界後，可瞬間加許多ans
            //printf("left:%d right:%d\n", left, right);
            if(right>left) ans += right-left;
            else product*=nums[right++];
            product /= nums[left];
        }
        return ans;
    }
};
//case 95/97: [57,44,92,28,66,60,37,33,52,38,29,76,8,75,22] 18
