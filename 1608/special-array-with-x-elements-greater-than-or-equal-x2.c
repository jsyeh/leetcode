// 好久不見，超喜歡 Easy 題！
// 題目給 nums[i]，問你「裡面有幾個數，剛好>=那個數」
// 比如說：有1個數，剛好>=1 。或是有3個數，剛好>=3 。找出那個數
int specialArray(int* nums, int numsSize) {
    for(int x=0; x<=numsSize; x++) {  // 先決定1個數x， 0...N 都試看看
        int bigger = 0;  // 查看 nums[i] 裡有幾個數 >=x
        for(int i=0; i<numsSize; i++) { // 逐個比較
            if(nums[i]>=x) bigger++;  // 找到了
        }
        if(x==bigger) return x;  // 找到答案了
    }
    return -1;
}
