// LeetCode 2229. Check if an Array Is Consecutive
// 檢測 nums 是否是「一串連續的整數」
int cmp(const void *p1, const void *p2) {
    return *(int*)p1 - *(int*)p2;
}
bool isConsecutive(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp);
    for(int i=1; i<numsSize; i++) {
        if(nums[i-1]+1 != nums[i]) return false;
    }
    return true;
}
