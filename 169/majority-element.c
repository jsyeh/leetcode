// 我照著 Boyer-Moore voting algorithm 試試
// 它可找到「過半」的那個數，原則是：挑個數，加加減減，變成0就重來
int majorityElement(int* nums, int numsSize) {
    int ans = nums[0], count = 1;
    for(int i=1; i<numsSize; i++){
        if(count==0) ans = nums[i]; //變成0就重來
        if(ans==nums[i]) count++;
        else count--;
    }
    return ans;
}
