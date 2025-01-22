// LeetCode 2529. Maximum Count of Positive Integer and Negative Integer
// 找出「有幾個正數」「有幾個負數」，大的那個數量回傳
int maximumCount(int* nums, int numsSize) {
    int pos = 0, neg = 0;
    for(int i=0; i<numsSize; i++) {
        if(nums[i]<0) neg++;
        if(nums[i]>0) pos++;
    }
    if(pos>neg) return pos;
    else return neg;
}
