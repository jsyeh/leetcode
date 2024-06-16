int minPatches(int* nums, int numsSize, int n) {
    int ans = 0, i = 0;
    long long int miss = 1; //因為數字可能超過 32 bit
    while(miss<=n){
        if(i<numsSize && nums[i]<=miss) {
            miss += nums[i]; //數字可能超過 32 bit
            i++;
        } else {
            ans += 1;
            miss += miss; //數字可能超過 32 bit
        }
    }
    return ans;
}
