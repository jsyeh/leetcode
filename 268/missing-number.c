//有n個數，0..n裡，少了1個數。有很多種寫法
//比如說，如果數字從小排到大，就可知「少了」什麼數
//比如說「修改陣列」來知道誰缺了。
//比如說用fast,slow來查看哪個數字有缺
//我直接用sort試試 --- 雖然慢，但想法簡單。
int cmp(const void *p1, const void *p2){
    return *(int*)p1 - *(int*)p2;
}
int missingNumber(int* nums, int numsSize) {
    qsort(nums,numsSize,sizeof(int),cmp);
    for(int i=0; i<numsSize; i++){
        if(nums[i]!=i) return i; //若沒逐一對到，表示缺了i
    }
    return numsSize; //0..(n-1)都沒缺，那就是缺n
}
