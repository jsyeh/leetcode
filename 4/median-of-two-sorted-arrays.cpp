class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int mid1 = (m+n+1)/2, mid2 = (m+n+2)/2;

        int i=0, j=0, ans1=0, ans2=0, pos=0, val=0;
        while(pos<mid2){
            if(i<m && j<n){
                if(nums1[i]<nums2[j]){
                    val = nums1[i];
                    i++;
                    pos++;
                }else{
                    val = nums2[j];
                    j++;
                    pos++;
                }
            }else if(i<m){
                val = nums1[i];
                i++;
                pos++;
            }else if(j<n){
                val = nums2[j];
                j++;
                pos++;
            }
            if(pos==mid1) ans1=val;
            if(pos==mid2) ans2=val;
        }
        return (ans1+ans2)/2.0;

    }
};
