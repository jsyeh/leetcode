int subsetXORSum(int* nums, int numsSize) {
    int bitORSum = 0;
    for(int i=0; i<numsSize; i++) {
        bitORSum |= nums[i];
    }
    return bitORSum * pow(2, numsSize-1);
}
