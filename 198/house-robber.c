int max(int a, int b){
    if(a>b) return a;
    else return b;
}
int rob(int* nums, int numsSize){
    if(numsSize==1) return nums[0];
    if(numsSize==2) return max(nums[0], nums[1]);
    int table[numsSize+1];//table[i] 如果有搶第i家，最多錢的組合
    table[0] = nums[0];
    table[1] = nums[1];
    table[2] = nums[0] + nums[2];
    for(int i=3; i<numsSize; i++){
        table[i] = nums[i] + max(table[i-2], table[i-3]);
    }
    return max(table[numsSize-1], table[numsSize-2]);
}//case 2/70: [0]
//case 5/70: [0,0]
