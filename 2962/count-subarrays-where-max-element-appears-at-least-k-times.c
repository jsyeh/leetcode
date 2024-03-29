long long countSubarrays(int* nums, int numsSize, int k) {
    int M = 0;
    for(int i=0; i<numsSize; i++){
        if(nums[i]>M) M = nums[i];
    }

    long long int ans = 0, tail = 0, MN = 0;
    for(int head=0; head<numsSize; head++){
        if(nums[head]==M) MN++;
        while(MN>=k){
            if(nums[tail]==M) MN--;
            tail++;
        }
        ans += tail;
    }
    return ans;
}
