int comp(const void *p1, const void *p2){
    return *(int*)p1 - *(int*)p2;
}
int abs(int a){
    if(a>0) return a;
    else return -a;
}
int threeSumClosest(int* nums, int numsSize, int target){
    qsort(nums, numsSize, sizeof(int), comp);

    int best = nums[0]+nums[1]+nums[2];
    for(int i=0; i<numsSize; i++){
        for(int j=i+1, k=numsSize-1; j<k;  ){
//printf("%d %d %d\n", i, j, k);
            int now = nums[i]+nums[j]+nums[k];
            if(abs(now-target)<abs(best-target)) best = now;

            if(now>=target) k--;
            else j++;
        }
    }
    return best;
}
