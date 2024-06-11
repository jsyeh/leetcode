// 找到最小值、最大值，算平均，去掉。
// 持續做，有幾個「不同」的平均。不過我不喜歡小數點，所以改用sum
int cmp(const void *p1, const void *p2) {
    return *(int*)p1 - *(int*)p2;
}
int distinctAverages(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp); //全部先sort
    int N = numsSize;
    for(int i=0; i<N/2; i++) {
        nums[i] += nums[N-1-i]; //加到左邊
    }
    qsort(nums, numsSize/2, sizeof(int), cmp); //前半再sort
    int ans = 1; //nums[0]這個數對應的總合，是第1個數
    for(int i=1; i<N/2; i++) {
        if(nums[i]!=nums[i-1]) ans++;  // 有不同，再++
    }
    return ans;
}
