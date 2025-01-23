// LeetCode 3375. Minimum Operations to Make Array Values Equal to K
// 每次可在 nums 挑個 valid 的數 h，比它大的數(都要相同)，都會變成 h
// 要讓 nums 裡全部的數都變成 k，最少要幾步？
// 問題等價成：如果把數字「小到大」排好，有幾個「不同」的數？要退幾步，才會變成k
int minOperations(int* nums, int numsSize, int k) {
    int table[101] = {};
    int ans = 0;
    for(int i=0; i<numsSize; i++) {
        if(nums[i]<k) return -1; // 如果有數比 k 小，那一定無法達成任務
        table[nums[i]]++;
        if(table[nums[i]]==1) ans++; // 多一個數要走
    }
    if(table[k]>0) ans--; // 還回去一個數，因可少走1步
    return ans;    
}
