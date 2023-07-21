//題目想了解有多少種排列組合。combo越多，排列組合越多
//比如說如果連續5個數字 combo 5-2=3，則123 234 345 1234 2345 12345 共3+2+1個可能
//也就是也就是 (1+combo)*combo/2
int numberOfArithmeticSlices(int* nums, int numsSize){
    if(numsSize<3) return 0;

    for(int i=0; i<numsSize-1; i++){
        nums[i] = nums[i+1] - nums[i]; //把數字，變成 diff值
    }

    int combo = 0, ans = 0;
    for(int i=0; i<numsSize-2; i++){
        if(nums[i]==nums[i+1]){
            combo++;
        }else{
            ans += (1+combo)*combo/2;
            combo = 0;
        }
    }
    ans += (1+combo)*combo/2; //最後的combo也要算

    return ans;
}
