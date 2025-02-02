// LeetCode 1752. Check if Array Is Sorted and Rotated
// 想確認 nums 裡，是否是「有排序好」可接受「稍微轉動」的結果 
// ex. 3,4,5,1,2就是好的。觀察發現相鄰兩兩比較，最多只會發生一次逆轉。
bool check(int* nums, int numsSize) {
    int bad = nums[numsSize-1] > nums[0];
    // 上面先判斷「頭尾項」，下面再判斷其他兩兩相鄰項
    for(int i=1; i<numsSize; i++) {
        if(nums[i-1] > nums[i]) bad++;
    }
    return bad <= 1;
}
