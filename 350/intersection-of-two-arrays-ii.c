/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int comp(const void *p1, const void *p2){
    return *(int*)p1 - *(int*)p2;
}
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    qsort(nums1, nums1Size, sizeof(int), comp);
    qsort(nums2, nums2Size, sizeof(int), comp);
    int* ans = (int*)malloc(nums1Size*sizeof(int));
    int N = 0;
    for(int i=0, j=0; i<nums1Size && j<nums2Size; ){
        if(nums1[i]==nums2[j]){
            ans[N++] = nums1[i];
            i++;
            j++;
        }else if(nums1[i]<nums2[j]){
            i++;
        }else if(nums1[i]>nums2[j]){
            j++;
        }
    }
    *returnSize = N;
    return ans;
}
