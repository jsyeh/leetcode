int max(int a, int b, int c){
    if(a>=b && a>=c) return a;
    if(b>=a && b>=c) return b;
    return c;
}
int min(int a, int b, int c){
    if(a<=b && a<=c) return a;
    if(b<=a && b<=c) return b;
    return c;
}
int maxProduct(int* nums, int numsSize){
    int max_so_far[numsSize], min_so_far[numsSize];

    max_so_far[0] = nums[0];
    min_so_far[0] = nums[0];

    int ans = max_so_far[0];
    for(int i=1; i<numsSize; i++){
        max_so_far[i] = max(nums[i], nums[i]*max_so_far[i-1], nums[i]*min_so_far[i-1]);
        min_so_far[i] = min(nums[i], nums[i]*max_so_far[i-1], nums[i]*min_so_far[i-1]);
        if(max_so_far[i]>ans) ans = max_so_far[i];
        //printf("%d: %d %d\n", nums[i], max_so_far[i], min_so_far[i]);
    }
    return ans;
}
