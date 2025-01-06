// LeetCode 1769. Minimum Number of Operations to Move All Balls to Each Box
// 字串 boxes 對應 n 個盒子（0空的、1有球）。若想分別「將球集中」在某個盒子，要分別移動幾步呢？
// 因盒子較少1000個，真的用暴力法，也能及時算完。
int* minOperations(char* boxes, int* returnSize) {
    int N = strlen(boxes); // 有 N 個盒子
    int* ans = (int*) malloc(sizeof(int)*N); // 放答案的陣列
    for(int i=0; i<N; i++) { // 針對 box i 要算出它的答案
        int now = 0;
        for(int j=0; j<N; j++) { // 巡視 box j
            if(boxes[j]=='1') { // 若有球，就更新答案
                if(i<j) now += j - i; // 距離
                else now += i - j; // 距離
            }
        }
        ans[i] = now; // 把答案放入 ans[i]
    }
    *returnSize = N; // C 在回傳陣列時，要標示「陣列的大小」
    return ans;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

