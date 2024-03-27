// nums 裡，subarray 乘起來要<k。問有幾種可能。
// 這種排列組合「有幾種」的問題，可用 left, right 來看
// 可以想像成毛毛蟲：右邊往右伸，左邊往右縮
// 主要迴圈，是要「左邊往右縮」還是「右邊往右伸」呢？
// 我一開始試「左邊往右縮」當成主要迴圈，結果程式要多2個if
// 所以我就改成「右邊往右伸」當成主要迴圈
int numSubarrayProductLessThanK(int* nums, int numsSize, int k) {
    int left = 0, right = 0;
    int p = 1; //left...right的product乘積,不會超過32bit
    int ans = 0; //有幾種可能
    for(right=0; right<numsSize; right++){ //逐格測試，以right往右伸為主迴圈
        p *= nums[right]; //right往右伸1格
        while(p>=k && left<=right){ //太大，且還能往右縮
            p /= nums[left++]; //left往右伸
        }//像毛毛蟲一樣，left會往右縮
        ans += right-left+1; //多這麼多種可能
    }
    return ans;
}
