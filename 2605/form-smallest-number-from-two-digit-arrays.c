// LeetCode 2605. Form Smallest Number From Two Digit Arrays
// nums1 和 nums2 「共有」的最小的數
// 或從 nums1 和 nums2 各挑1個數，組合出的2位數「要最小」
int minNumber(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int freq1[10] = {}, freq2[10] = {}; // 先統計數字出現次數
    for(int i=0; i<nums1Size; i++) {
        freq1[nums1[i]]++;
    }
    for(int i=0; i<nums2Size; i++) {
        freq2[nums2[i]]++;
    }
    int d1 = -1, d2 = -1;
    for(int i=1; i<=9; i++) { // 從1到9巡，若出現2次，表示剛好都有，便是答案
        if(freq1[i]==1 && freq2[i]==1) return i;
        if(d1==-1 && freq1[i]==1) d1=i;
        if(d2==-1 && freq2[i]==1) d2=i;
    }
    // 若沒有共有的數，那就挑「最小的數」再組起來
    if(d1<d2) return d1*10+d2;
    else return d2*10+d1;
}
