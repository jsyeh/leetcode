int missingInteger(int* nums, int numsSize) {
    int prefix = nums[0]; // 一開始 prefix 先放第1個數
    for(int i=1; i<numsSize; i++){ //照題目，找合理的prefix sum
        if(nums[i-1]+1==nums[i]) prefix += nums[i];
        else break;
    }
    //因為只有50個數字
    int exist[53]={}; //做對照表，看有哪些數字存在
    for(int i=0; i<numsSize; i++) exist[nums[i]]=1;

    int ans = prefix; //開始逐項檢查
    while(ans<51 && exist[ans]==1){ //只要數字存在
        ans++; //就繼續查看下一個數
    }
    return ans;
}
//case 2/616: [29,30,31,32,33,34,35,36,37]
// 數字不能太大
