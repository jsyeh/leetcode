bool isMajorityElement(int* nums, int numsSize, int target){

    int count=0;
    for(int i=0; i<numsSize; i++){
        if(nums[i]==target) count++;
    }
    if(count>numsSize/2) return true;
    else return false;
}
