// LeetCode 2455. Average Value of Even Numbers That Are Divisible by Three
// nums 裡，找到所有「偶數、且為3的倍數」，其實就是「找6個倍數」的平均
int averageValue(int* nums, int numsSize) {
    int total = 0, N = 0;
    for(int i=0; i<numsSize; i++) {
        if(nums[i]%6==0){
            total += nums[i];
            N++;
        }
    }
    if(N==0) return 0;
    return total / N;
}
