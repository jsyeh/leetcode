class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] ans = new int[m+n];
        for(int i=0, j=0, k=0; i<m || j<n;  ){
            if(i==m){
                while(j<n){
                    ans[k++] = nums2[j++];
                }
                break;
            }else if(j==n){
                while(i<m){
                    ans[k++] = nums1[i++];
                }
                break;
            }
            if(nums1[i] <= nums2[j]){
                ans[k++]=nums1[i++];
            }else ans[k++]=nums2[j++];
        }
        for(int i=0; i<m+n; i++){
            nums1[i] = ans[i];
        }
    }
}
