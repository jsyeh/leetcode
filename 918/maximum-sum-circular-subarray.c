int maxSubarraySumCircular(int* nums, int numsSize){
    int N = numsSize;
    int table[N];
    table[0] = nums[0];//有包含nums[0] 的最大值
    int ans = nums[0];
    for(int i=1; i<N; i++){
        int temp = nums[i] + table[i-1];
        if(temp>nums[i]) table[i] = temp;
        else table[i] = nums[i];
        if(table[i]>ans) ans = table[i];
    }

    //如果不小心頭尾相接才是答案時，要有第2種算法：算最小值，再減
    //這個想法，來自這題的 Editorial 的 Algorithm 2
    //不過有個例外，就是如果最小值是 all 全算的話，算例外哦！
    int totalSum = 0;
    for(int i=0; i<N; i++) totalSum += nums[i];

    int table2[N];
    table2[0] = nums[0];
    int ans2 = nums[0];
    for(int i=1; i<N; i++){
        int temp = nums[i] + table2[i-1];
        if(temp<nums[i]) table2[i] = temp;
        else table2[i] = nums[i];
        if(table2[i]<ans2) ans2 = table2[i];
    }
    //printf("ans2:%d\n", ans2);
    if(totalSum == ans2) return ans; //因為全算不合理，所以用ans值

    if(totalSum - ans2 > ans) ans = totalSum - ans2;

    return ans;
}
