int max(int a, int b){
    if(a>b) return a;
    else return b;
}
int maxUncrossedLines(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int table[nums1Size+1][nums2Size+1];
    for(int i=0; i<=nums1Size; i++) table[i][0] = 0;
    for(int j=0; j<=nums2Size; j++) table[0][j] = 0;

    for(int i=1; i<=nums1Size; i++){
        for(int j=1; j<=nums2Size; j++){
            if(nums1[i-1]==nums2[j-1]) table[i][j] = table[i-1][j-1] + 1;
            else {
                table[i][j] = max(table[i-1][j], table[i][j-1]);
            }
        }
    }
    return table[nums1Size][nums2Size];
}
//case 61/74: [1] [3]
