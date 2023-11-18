//先將 nums 從小到大排好，接下來左到右巡一輪，每次決定右邊界後，再找左邊界
// 右邊界-左邊界+1 便是（在k個操作後）會重覆的次數。找最大的次數
int cmp(const void *p1, const void *p2) {
    return *(int*)p1 - *(int*)p2;
}
int maxFrequency(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int), cmp); //先將 nums 從小到大排好
    //for(int i=0; i<numsSize; i++) printf("%d ", nums[i]); //看排序結果

    //Running Sum 方便算 nums[left]...nums[right] 的總和
    long long int runSum[numsSize+1]; //GNU C++ 可接受此語法
    runSum[0] = 0; 
    //printf("\n0 "); //看runSum結果
    for(int i=0; i<numsSize; i++) { //為後面簡化程式，讓 runSum[0]=0
        runSum[i+1] = runSum[i] + nums[i]; 
        //runSum[right+1]-runSum[left] 歪一格 即 nums[left]+...+nums[right]
        //printf("%d ", runSum[i+1]); //看runSum結果
    }
    long long int left = 0, ans = 1;
    for(int right = 0; right < numsSize; right++) {
        //while(runSum[right]-runSum[left]>k) {
        while(runSum[right+1]-runSum[left]+k<nums[right]*(right-left+1)) { 
            //nums[left]+...+nums[right] 即 runSum[right+1]-runSum[left] 歪一格
            left++; //將左邊界往右滑
        }
        if(right-left+1>ans) ans = right-left+1; //nums[left]...nums[right]有幾個數
    }
    return ans;
}
//case 3/71: [9940,9995,9944,9937,9941,9952,9907,9952,9987,9964,9940,9914,9941,9933,9912,9934,9980,9907,9980,9944,9910,9997] 7925
//case 56/71: 數字超級大，有可能超過 32 bit, 所以要 long long int
