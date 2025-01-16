// LeetCode 2425. Bitwise XOR of All Pairings
// nums1 和 nums2 裡有「很多數」，左右排列組合配對 XOR 結果放在 nums3
// 問 nums3 裡「全部的數」XOR 的結果
int xorAllNums(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int ans = 0; // 其實，就看 XOR 幾次即可。XOR兩次，等於「沒有」XOR，所以只看「奇數」
    if(nums2Size%2==1) { // 右邊是奇數時，左邊的數，才會「都算1次」
        for(int i=0; i<nums1Size; i++) { 
            ans ^= nums1[i];
        }
    }
    if(nums1Size%2==1) { // 左邊是奇數時，右邊的數，才會「都算1次」
        for(int i=0; i<nums2Size; i++) {
            ans ^= nums2[i];
        }
    }
    return ans;
}
