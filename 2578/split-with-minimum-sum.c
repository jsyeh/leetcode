// LeetCode 2578. Split With Minimum Sum
// 把數字，分成2個數，希望數字「加起來」最小
int cmp(const void*p1, const void*p2) {
    return *(int*)p1 - *(int*)p2;
}
int splitNum(int num) {
    int a[10] = {}, N = 0;
    while(num>0) {
        if(num%10>0) a[N++] = num%10; // 把非0項加入
        num /= 10;
    }
    qsort(a, N, sizeof(int), cmp);
    int ans = 0;
    if(N%2==1) {
        ans = a[0]; // 奇數項，會多1位，先處理
        for(int i=1; i<N; i+=2) { // 再平均分配
            ans = ans * 10 + a[i] + a[i+1];
        }
        return ans;
    } else { // 偶數項
        for(int i=0; i<N; i+=2) { // 平均分配
            ans = ans * 10 + a[i] + a[i+1];
        }
        return ans;
    }

}
