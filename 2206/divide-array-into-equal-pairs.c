// LeetCode 2206. Divide Array Into Equal Pairs
// 將 nums 裡的數，相同的數「兩兩一組」分好，全部分完。
bool divideArray(int* nums, int numsSize) {
    int count[501] = {};
    int odd = 0; // 迴圈前面「還沒有落單的數」
    for(int i=0; i<numsSize; i++) {
        count[nums[i]]++;
        if(count[nums[i]]%2==0) odd++;
        else odd--; // 迴圈中間，即時更新「有幾個落單的數」
    }
    return odd==0; // 迴圈後面，確認沒有任何落單的數
}
