// LeetCode 2367. Number of Arithmetic Triplets
// 請問有幾組 i<j<k 使得 nums[i] nums[j] nums[k] 距離 diff
// 用暴力3層迴圈，太慢了。因為 nums[i] 是「嚴格遞增」越來越大
// 所以一定不會重覆，可利用 history 來記下「之前出現過的數」
int arithmeticTriplets(int* nums, int numsSize, int diff) {
    int ans = 0;
    int history[201] = {};
    for(int i=0; i<numsSize; i++){
        if(nums[i]-diff*2>=0){
            if(history[nums[i]-diff]==1 && history[nums[i]-diff*2]==1) ans++;
        }
        history[nums[i]] = 1;
    }

    return ans;
}
