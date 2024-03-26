int returnToBoundaryCount(int* nums, int numsSize) {
    int ant = 0, ans = 0; //ant所在位置，ans:回到0的次數
    for(int i=0; i<numsSize; i++){
        ant += nums[i];
        if(ant==0) ans++;
    }
    return ans;
}
