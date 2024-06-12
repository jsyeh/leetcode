//方法1: 泡泡排序法
void sortColors(int* nums, int numsSize) {
    for(int k=0; k<numsSize-1; k++){
        for(int i=0; i<numsSize-1; i++){
            if(nums[i] > nums[i+1]){
                int temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
            }
        }
    }
}
