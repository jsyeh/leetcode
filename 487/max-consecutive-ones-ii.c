int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int left = 0, right = 0; // 右不包含
    int zero = 0, one = 0, ans = 0;
    while(right<numsSize){ // 右邊還沒撞到邊界
        if(nums[right]==1) { // 是1，太好了
            right += 1;
            one += 1;
        } else if(nums[right]==0 && zero==0) { // 是0也是可以啦，但只有1個quota
            right += 1;
            zero += 1;
        } else { // 這是 zero超標的狀況
            right += 1;
            zero += 1; // 很遺憾，現在 zero 超標了
            while(zero > 1) { // 只要超標，就持續吐出 nums[left]
                if (nums[left]==0) zero -= 1; // 吐出 zero
                else one -= 1; // 吐出 one
                left += 1; // 吐出後，改變 left 的位置
            }
        }
        printf("left:%d right:%d zero:%d one:%d\n", left, right, zero, one);
        if(one + zero > ans) ans = one + zero;
    }      
    return ans;       
}
