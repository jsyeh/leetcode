// LeetCode 260. Single Number III
// 今天題目, 要找出「只出現一次」的數字, 應有多種寫法
// 題目解釋「所有數字都出現2次, 只有2個數出現1次」
// 在 C 語言版本我換另一種寫法, 用 sort() 先排好, 再排除「連續2個相同的數」
int cmp(const void*p1, const void*p2) {
    if( *(int*)p1 > *(int*)p2 ) return 1;
    if( *(int*)p1 < *(int*)p2 ) return -1;
    return 0; //給 qsort() 比大小的函式
}
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int * ans = (int*) malloc(sizeof(int)*2); 
    *returnSize = 2;  // 在 LeetCode 的 C 語言版本, 要求要自己用指標管理memory
    int ansN = 0;  // 答案目前填完幾個

    qsort(nums, numsSize, sizeof(int), cmp);  // 數字從小到大排好

    for(int i=0; i<numsSize-1; i++) {  // 再逐一巡排好的數, 相同的數會變「鄰居」
        if(nums[i]==nums[i+1]) i++; // 遇到相同的數, 就多跳1格, 避開它們
        else {
            ans[ansN++] = nums[i]; //數字不相同, 就可以記下來
        }
    }
    if(ansN==1) ans[1] = nums[numsSize-1];  // 題目保證有2個答案。若少1個的話, 補沒巡到的最後1數
    return ans;
}
// case 8/33: [1,1,0,-2147483648] 超級大的數數, 
