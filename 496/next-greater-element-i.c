/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextGreaterElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    for(int i=0; i<nums1Size; i++){
        int now = nums1[i];
        int j=0;
        for(  ; j<nums2Size; j++){
            if(now==nums2[j]){
                break;
            }
        }
        int ans = -1;
        for(  ; j<nums2Size; j++){
            if(nums2[j]>now) {
                ans = nums2[j];
                break;
            }
        }
        nums1[i] = ans;
    }
    *returnSize = nums1Size;
    return nums1;
}
