int lengthOfLIS(int* nums, int numsSize){
    int table[numsSize+1];//table[i]表示包含i-th 的最長的值
    int ans = 1;
    table[0] = 1;//包含 nums[0] 的LIS的結果
    for(int i=1; i<numsSize; i++){
        int temp=0;
        for(int k=0; k<i; k++){
            if(nums[k]<nums[i] && table[k]>temp) temp=table[k];
        }
        table[i] = temp + 1;
        if(table[i]>ans) ans = table[i];
    }
    return ans;
}//case 53/54: [0]
