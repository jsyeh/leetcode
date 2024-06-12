// 方法2: Bucket Sort 桶子排序法
void sortColors(int* nums, int numsSize) {
    int zero=0, one=0, two=0;  //準備3個桶子,分別裝 0, 1, 2 有幾個
    for(int i=0; i<numsSize; i++){
        if(nums[i] == 0) zero++; //找到1個0
        if(nums[i] == 1) one++;  //找到1個1
        if(nums[i] == 2) two++;  //找到1個2
    }
    for(int i=0; i<numsSize; i++){ //最後再放回去、排好
        if(i<zero) nums[i] = 0; //最左邊,都放0
        else if(i<zero+one) nums[i] = 1; //剩下的中間,放1
        else nums[i] = 2; //剩下右邊, 放2
    }
}
