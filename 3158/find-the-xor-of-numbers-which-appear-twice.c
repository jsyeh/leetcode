// LeetCode 3158. Find the XOR of Numbers Which Appear Twice
// 找到 nums 裡「剛好出現2次」的數, 全部用 XOR 混起來。
// 因數字很少(最多50個數), 且介於 1..50之間, 所以開個陣列, 這題就搞定了。
// 記下「數字出現的次數」,看誰出現2次
int duplicateNumbersXOR(int* nums, int numsSize) {
    int table[51] = {};  // 陣列從 0 開始, 所以要開 51格, 裝1..50之間的數
    for(int i=0; i<numsSize; i++) {
        table[nums[i]] ++;  // 數字出現次數 +1
    }
    int ans = 0;
    for(int i=1; i<=50; i++) {  // 巡第2次, 看 table 裡的每個數
        // 查看 table[i] 裡, 有誰「剛好出現2次」, 就要用 XOR 混到答案裡
        if(table[i]==2) ans = ans ^ i;
    }
    return ans;
}
