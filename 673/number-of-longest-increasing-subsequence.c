int findNumberOfLIS(int* nums, int numsSize){
    int table[numsSize]; //LIS的長度
    int combination[numsSize+1]; //LIS的組合數，包含i格的LIS有幾種可能
    int LISlen = 1;
    table[0] = 1;
    combination[0] = 1;
    for(int i=1; i<numsSize; i++){
        int temp=0;
        for(int k=0; k<i; k++){
            if(nums[k]<nums[i] && table[k]>temp) temp = table[k];
        }
        table[i] = temp +1;
        combination[i] = 0;
        for(int k=0; k<i; k++){
            if(table[k] == temp && nums[k]<nums[i]) combination[i] += combination[k];
        }
        if(combination[i]==0) combination[i] = 1;//若不是從前面推出來，自己有獨立1種解法

        if(table[i]>LISlen){
            LISlen = table[i];
        }
    }
    int ans=0;
    for(int i=0; i<numsSize; i++){
        if(table[i]==LISlen) ans+=combination[i];
    }
    return ans;
}//case 29/223: [1,2,4,3,5,4,7,2]
