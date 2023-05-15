int maxDistance(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int ans = 0;
    for(int i=0, j=0; i<nums1Size && j<nums2Size; ){
        if(nums1[i]<=nums2[j]){
            if(j>=i){
                int temp = j-i;
                if(temp>ans) ans = temp;
            }
            j++;
        }else if(nums1[i]>nums2[j]) i++;
    }
    return ans;
}
