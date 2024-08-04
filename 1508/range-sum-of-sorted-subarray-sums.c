// LeetCode 1508. Range Sum of Sorted Subarray Sums
// nums 裡有1000個數，把裡面全部可能的subarray nums[i]...nums[j] 都加起來
// 把加起來的全部數「從小到大排好」。最後再把 left...right 加好。
// 要計算 left...right(包含) 1-index 加總
// 這題就「順順」照著題目描述來做，就成功了！
int cmp(const void*p1, const void*p2) {
    return *(int*)p1 - *(int*)p2;
}
int rangeSum(int* nums, int numsSize, int n, int left, int right) {
    int table[n*n], N=0;
    for(int i=0; i<n; i++){ // 決定開始的 nums[i]
        int preSum = 0; // 放 nums[i]...nums[j] 加總
        for(int j=i; j<n; j++){
            preSum += nums[j]; // 利用 preSum 持續累積
            table[N++] = preSum; // 加總 nums[i]...nums[j]這段的和
        }
    }
    qsort(table, N, sizeof(int), cmp); // 照題目要求，從小到大排好
    int ans = 0;
    for(int i=left-1; i<right; i++) { // 要把 1-index 轉成陣列的 0-index，所以 left-1
        ans = (ans + table[i]) % 1000000007; // 怕數太大，題目要取餘數
    }
    return ans;
}

