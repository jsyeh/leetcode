int cmp(const void*p1, const void*p2) {
    return *(int*)p1 - *(int*)p2;
}
char* triangleType(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp);
    if(nums[0]+nums[1]<=nums[2]) return "none";
    else if(nums[0]==nums[1] && nums[1]==nums[2]) return "equilateral";
    else if(nums[0]==nums[1] || nums[1]==nums[2]) return "isosceles";
    else if(nums[0]+nums[1]>nums[2]) return "scalene";
    else return "none";
}
