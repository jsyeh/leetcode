/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// LeetCode 2028. Find Missing Observations
// 丟n+m個骰子，有n個miss沒看到，但有mean平均值。找出miss掉的n個值
int ans[100000];
int* missingRolls(int* rolls, int rollsSize, int mean, int n, int* returnSize) {
    // 要從 m 個 rolls[i] 的值，及總平均值mean，找出n個miss值
    int total = mean * (rollsSize+n);
    int now = total; //現在「將要剩下」給n個數的量
    for(int i=0; i<rollsSize; i++) now -= rolls[i]; //用掉，就扣掉

    if(now<n || now>n*6){ //會導致「無法用骰子1-6來呈現」
        *returnSize = 0;
        return ans;
    }
    //現在now要分給n個骰子
    int base = now / n, diff = now % n;

    // base 是大家基礎的有的數，diff 是多出來的數，要再分配出去
    for(int i=0; i<diff; i++) ans[i] = base + 1; //前面的平分「多出來的數」
    for(int i=diff; i<n; i++) ans[i] = base; //後面就基礎的數就好了

    *returnSize = n;
    return ans;
}
