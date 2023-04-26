int sumOfDigits(int* nums, int numsSize){
    int min = nums[0];
    for(int i=0; i<numsSize; i++){
        if(nums[i]<min) min = nums[i];
    }
//printf("min:%d\n", min);
    int sum=0;
    while(min>0){
        sum += min%10;
        min = min / 10;
    }
    if(sum%2==1) return 0;
    else return 1;
}
