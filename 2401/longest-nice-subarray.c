// LeetCode 2401. Longest Nice Subarray
// 想找「最長的連續subarray」裡「任兩數」bitwise AND 為 0
// 也就是，連續subarray裡，所有數「都不能用到相同的bit」
// 今天的主題是 bit 相關，使用 & | ^ 來做，配合「毛毛蟲」來找答案。
int longestNiceSubarray(int* nums, int numsSize) {
    int usedBit = 0, ans = 1;
    for(int i=0, j=0; i<numsSize; i++) { // 用 for 迴圈，讓右邊頭往右進
        while((usedBit & nums[i]) != 0) { // 身體不舒服（要小心圓括號）
            usedBit ^= nums[j++]; // 就吐掉左邊尾巴 nums[j]
        }
        usedBit |= nums[i]; // 正式將右邊頭 nums[i] 加入
        if(i-j+1>ans) ans = i-j+1; // 更新答案的長度
    }
    return ans;
}
