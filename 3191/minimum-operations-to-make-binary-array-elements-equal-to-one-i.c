// LeetCode 3191. Minimum Operations to Make Binary Array Elements Equal to One I
// 想把 nums 裡的數，每次「切換3個相鄰的數」0與1互換，要做幾次「3個數翻牌」才能全部變成1
int minOperations(int* nums, int numsSize) {
    int ans = 0; // 要「翻牌翻幾次」
    for(int i=0; i<numsSize-2; i++) {
        if(nums[i]==0){ // 遇到0要翻牌
            ans++; // 翻牌加一次
            nums[i+1] = 1 - nums[i+1]; //反過來
            nums[i+2] = 1 - nums[i+2]; //反過來
        }
    }
    int N = numsSize;
    if(nums[N-1]==0 || nums[N-2]==0) return -1; //最後有0失敗
    return ans; //可以成功「翻牌」全部變成1
}

