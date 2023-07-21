//這題不是算 LIS 的長度，而是算 LIS 有幾種可能的走法
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int N = nums.size();
        int LIS[N]; //LIS[i]: 最後一位為nums[i] 的 LIS 長度
        int possible[N]; // possible[i] 表示nums[i]結尾，且LIS為LIS[i]的可能走法
        //LIS[0] = 1; //只有 nums[i] 的長度
        //possible[0] = 1; //就1種可能
        int maxLIS = 0;
        for(int i=0; i<nums.size(); i++){
            LIS[i] = 1;
            for(int k=0; k<i; k++){
                if(nums[i]>nums[k] && LIS[k]+1>LIS[i]) {
                    LIS[i] = LIS[k]+1;
                }
            }//離開迴圈時，便確定此層的 LIS 值
            if(LIS[i]>maxLIS) maxLIS = LIS[i];
            possible[i] = 0;
            for(int k=0; k<i; k++){
                if(nums[i]>nums[k] && LIS[k]+1==LIS[i]) {
                    possible[i] += possible[k]; //LIS[k] 可組合出 LIS[i]
                }
            }
            if(possible[i]==0) possible[i] = 1; //若都無法組合，則自己1組
        }
        //已經查出 LIS 的值，是否同時也記錄 table[i] 表示 LIS的組合
        int ans = 0;
        for(int i=0; i<N; i++){
            //printf("LIS:%d (%d) ", LIS[i], possible[i]);
            if(LIS[i] == maxLIS) ans+=possible[i];
        }
        return ans;
    }
};
//case 216/223: [1] 所以迴圈要從0開始，不能從1開始，不然會漏掉它
