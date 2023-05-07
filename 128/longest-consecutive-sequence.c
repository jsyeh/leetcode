int comp(const void *p1, const void *p2){
    return *(int*)p1 - *(int*)p2;
}
int longestConsecutive(int* nums, int numsSize){
    if(numsSize==0) return 0;

    qsort(nums, numsSize, sizeof(int), comp);
    int N=1;
    for(int i=1; i<numsSize; i++){
        if(nums[N-1]!=nums[i]){
            nums[N] = nums[i];
            N++;
        }
    }

    int ans=1, len=1;
    for(int i=1; i<N; i++){
        if(nums[i-1]+1==nums[i]){
            len++;
        }else{
            if(len>ans) ans = len;
            len=1;
        }
    }
    if(len>ans) ans = len;
    return ans;
}
