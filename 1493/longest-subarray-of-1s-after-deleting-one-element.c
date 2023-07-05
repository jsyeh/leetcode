//這題偷看 lee215 的解法，實在是太優美了
//https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/708112/java-c-python-sliding-window-at-most-one-0/
//它的想法是，有個「最多1的框框」（裡面最多只能有1個zero)，會往右移
//像貪食蛇一樣，如果合乎(裡面只能有1個zero)條件，就能長長
int longestSubarray(int* nums, int numsSize){
    int left=0, right=0, zero=0;
    for(int i=0; i<numsSize; i++){
        if(nums[i]==1) right++;
        else if(nums[i]==0){
            zero++; //多了一個0
            right++; //不管遇到誰，右界一直右移，拉著框框走or長大
        }

        if(zero>1){//不幸裡面有很多0的話，
        //這個「最多1的框框」就(保持原本大小)右移，直到吐出足夠多的zero
            if(nums[left]==0) zero--; //吐出1個zero
            left++;
        }
    }
    return right-left - 1;//因為要扣掉一個 zero (不能不扣掉)
    //就算全部都是1,也要扣掉一個，因為題目要說一定要掉掉一個數,1個1就被犠牲
}
