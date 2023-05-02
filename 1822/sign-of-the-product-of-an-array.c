//LeetCode 1822. Sign of the Product of an Array 想看乘起來的正負號
int arraySign(int* nums, int numsSize){
    int ans = 0; //有幾個 <0 的負數?
    for(int i=0; i<numsSize; i++){
        if(nums[i] < 0) ans++;
        if(nums[i]==0) return 0;//提早結束囉! 0沒救了
    }
    if(ans%2==1) return -1;
    else return 1;
}
