int maxSubArray(int* nums, int numsSize){
    //Idea: table[i] 表示：要包含 nums[i]，之前最大sum
    // 有兩種可能：nums[i] 是新的開始 or 其實要接到前面 table[i-1]
    int table[numsSize]; //開好 Dynamic Programming 需要的表格
    table[0] = nums[0]; 
    int ans = table[0]; //一邊做 dynamic programming, 一邊巡，找到最大的答案
    for(int i=1; i<numsSize; i++){
        int temp = nums[i] + table[i-1];
        if(temp>nums[i]) table[i] = temp;
        else table[i] = nums[i];

        if(table[i]>ans) ans = table[i]; //如果答案更好，就更新
    }
    return ans;
}
