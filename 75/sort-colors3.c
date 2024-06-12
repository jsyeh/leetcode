// LeetCode 75. Sort Colors 色彩 0,1,2 照著排序。其實不用真的排序
// 只要先數一數：有幾個0 幾個1 幾個2，再依序放回 nums[i] 即可
// 這個方法又叫 Bucket Sort 桶子排序法/Couting Sort 計數排序法
// 註：題目要求，不要使用預設的 sort library
void sortColors(int* nums, int numsSize) {
    int H[3] = {}; //準備3個桶子,分別裝 0, 1, 2 （對應有幾個）
    for(int i=0; i<numsSize; i++){
        H[nums[i]]++;
    }
    //最後再放回去、排好
    for(int i=0; i<numsSize; i++){
        if(i<H[0]) nums[i] = 0;
        else if(i<H[0]+H[1]) nums[i] = 1;
        else nums[i] = 2;
    }
}
