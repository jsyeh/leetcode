bool isMonotonic(int* nums, int numsSize){
    if(numsSize==1) return true;
    int bigger=0, smaller=0;
    for(int i=1; i<numsSize; i++){
        if(nums[i]-nums[i-1]>0) bigger++;
        if(nums[i]-nums[i-1]<0) smaller++;
    }
    if(bigger==0 || smaller==0) return true;
    else return false;
}
