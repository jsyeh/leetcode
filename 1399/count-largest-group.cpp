// LeetCode 1399. Count Largest Group
class Solution {
public:
    int countLargestGroup(int n) {
        int max_count = 0; // 數一下, 統計最多的, 是出現幾次
        int a[100] = {}; // 陣列宣告, 放「加總的total」有出現幾次
        for(int i=1; i<=n; i++) { // 人類的 for 迴圈, 從1...n
            int total = 0, now = i; // 加起來的結果叫 total, 現在的數 now
            while( now > 0 ){ // 剝皮法, 如果 now 還有剩, 繼續剝
                total += now % 10;  // 把「皮」加起來(每一位數都加起來嘛)
                now = now / 10; // 剝完皮, 數字就變小囉~
            }
            a[total]++; // 統計結果多1個total的加起來的值 total 拿來用!!
            if(a[total] > max_count) max_count = a[total]; // max_count 放最多的數
        }
        int ans = 0; // 最後找答案找出來 (出現最多次數的次數, 有幾個數)
        for(int i=0; i<100; i++) { // 巡一下陣列 a[i] 裡面, 剛好是最大值 max_count 的話
            if(a[i]==max_count) ans++; // 就多一個最大的數
        }
        return ans;
    }
};
