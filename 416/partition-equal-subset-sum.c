bool canPartition(int* nums, int numsSize){
    int total=0;
    for(int i=0; i<numsSize; i++){
        total += nums[i];
    }
    if(total%2==1) return false; //奇數，一定無法分成兩群

    //現在目標：看數字nums[i]能到達的數字有哪些, table[total/2]
    bool table[total+1];
    for(int i=0; i<=total; i++){
        table[i] = false;
    }
    table[0] = true;

    int currBig=0;
    for(int i=0; i<numsSize; i++){
        int now = nums[i];
        for(int k=total-now; k>=0; k--){
            if(table[k]==true) table[k+now]=true;
        }
    }
    return table[total/2];
}
