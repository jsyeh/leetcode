// 題目：要讓 nums[i] 全部 XOR 起來，希望是k
// 問需先將 bit 改幾次，才做得到
// 這題超簡單的，因 XOR 的效果，其實就是「把對應bit反過來」
// 所以「希望最後能變成 k 」就把 k 拿去對 nums 每個num都做XR
// 最後再數一數「有幾個bit是1」就得到答案了。
int minOperations(int* nums, int numsSize, int k) {
    for(int i=0; i<numsSize; i++) {
        k ^= nums[i];  // 先逐項 XOR 累積出結果
    }  // 最後離開時，看k有幾個bit是1，便能知道答案
    int ans = 0;
    while(k>0) {  // 使用剝皮法，來數數「有幾個bit是1」
        ans += k % 2;  // 是1的話，就加起來，對應 operation的次數
        k /= 2;  // 剝皮後，數字就變小了
    }
    return ans;
}
