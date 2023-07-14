class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int positive_len[nums.size()];
        int negative_len[nums.size()];
        int ans = 0;
        if(nums[0]>0) {
            positive_len[0] = 1;
            negative_len[0] = 0;
            ans = 1;
        } else if(nums[0]<0) {
            positive_len[0] = 0;
            negative_len[0] = 1;
        } else {
            positive_len[0] = 0;
            negative_len[0] = 0;
        }

        for(int i=1; i<nums.size(); i++) {
            if(nums[i]>0) {
                positive_len[i] = positive_len[i-1] + 1;
                negative_len[i] = negative_len[i-1] + 1;
                //因為有例外，也就是前一步沒有 negative 的話，不可能 +1, 所以歸零
                if(negative_len[i-1]==0) negative_len[i] = 0;
            } else if(nums[i]<0) {
                negative_len[i] = positive_len[i-1] + 1;
                positive_len[i] = negative_len[i-1] + 1;
                //因為有例外，也就是前一步沒有 negative 的話，不可能 +1, 所以歸零
                if(negative_len[i-1]==0) positive_len[i] = 0;
            } else {
                positive_len[i] = 0;
                negative_len[i] = 0;
            }
//printf("positive: %d negative: %d\n", positive_len[i], negative_len[i]);
            if(positive_len[i]>ans) ans = positive_len[i];
        }
        return ans;
    }
};
//case 67/112: [-16,0,-5,2,2,-13,11,8]
