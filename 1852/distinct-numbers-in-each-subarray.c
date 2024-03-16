// 「相鄰k個數」裡，有幾個「不同的數」
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* distinctNumbers(int* nums, int numsSize, int k, int* returnSize){
    int counter[100001] = {}; //目前 sliding window 裡各個數出現的次數。初始0
    int dist = 0; //現在不同的數的數目
    for(int i=0; i<k; i++){ //先完成前k項統計，並更新nums[0]
        counter[nums[i]]++;
        if(counter[nums[i]]==1) dist++; //不同的數的數目增加了
    }
    int prev = nums[0]; //因為迴圈裡需要用到 nums[0] 或 nums[i-k] 所以要先備分
    nums[0] = dist; //有幾個不同的數
    for(int i=k; i<numsSize; i++){
        counter[prev]--;//糟，nums[0]或nums[i-1]稍早改過，造成問題，所以改用prev
        if(counter[prev]==0) dist--;
        counter[nums[i]]++;
        if(counter[nums[i]]==1) dist++; //不同的數的數目增加了
        prev = nums[i-k+1]; //備份 prev = nums[i-k+1]
        nums[i-k+1] = dist; //再蓋掉nums[i-k+1]
        //printf("%d ", nums[i-k+1]);
    }
    * returnSize = numsSize - k + 1; //要 return 的陣列長度
    return nums; //回收、再利用陣列
}
