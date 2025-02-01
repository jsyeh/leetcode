// LeetCode 3151. Special Array I
// 希望 nums 裡，每2個相鄰的數 parity 都不同（奇數、偶數交錯）
// 所以相鄰2數加起來，一定要是奇數
bool isArraySpecial(int* nums, int numsSize) {
    for(int i=0; i<numsSize-1; i++) {
        if((nums[i]+nums[i+1]) % 2 == 0) return false;
    }// 若加起來是「偶數」，就失敗
    // 都沒有失敗，就是成功
    return true;
}
