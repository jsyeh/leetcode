// 找到「最接近0」的數
int findClosestNumber(int* nums, int numsSize) {
    int ans = nums[0]; // 先隨便挑個數，當答案
    for(int i=1; i<numsSize; i++){
        if(abs(nums[i])<abs(ans)) ans = nums[i];
        else if(abs(nums[i])==abs(ans) && nums[i]>ans) ans = nums[i];
    }
    return ans;
}
