// LeetCode 2367. Number of Arithmetic Triplets
// 請問有幾組 i<j<k 使得 nums[i] nums[j] nums[k] 距離 diff
int arithmeticTriplets(int* nums, int numsSize, int diff) {
    int ans = 0;
    for(int i=0; i<numsSize-2; i++){
        for(int j=i+1; j<numsSize-1; j++){
            for(int k=j+1; k<numsSize; k++){
                if(nums[j]-nums[i]==diff && nums[k]-nums[j]==diff) ans++;
            }
        }
    }
    return ans;
}
