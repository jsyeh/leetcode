// 有兩組陣列 nums1 nums2 裡面有一堆數字
// return 它們的「交集」有哪些數字
// 使用 C 的話，不容易使用 HashMap 來加速
// 因為 數字範圍 <=1000 可開陣列來解決
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int used[1001] = {}; //先都清為0，若有出現，則把數字設為1
    int ansN = 0; //答案打算放在 nums1 重覆利用
    for(int i=0; i<nums1Size; i++){ //先巡第1個陣列
        used[nums1[i]] = 1; //標注有在 nums1 出現
    }
    for(int i=0; i<nums2Size; i++){ //再巡第2個陣列
        if(used[nums2[i]]==1){ //這麼巧，剛好這個數也有在nums1出現
            used[nums2[i]] = 0; //用過的話，就清空
            nums1[ansN++] = nums2[i]; //把它移到nums1當答案
        }//回收、重覆利用 nums1 的陣列記憶體，就不用自己開
    }
    *returnSize = ansN;
    return nums1; //回收、重覆利用 nums1 的陣列記憶體，就不用自己開
}
