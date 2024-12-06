// LeetCode 2554. Maximum Number of Integers to Choose From a Range I
// 挑 1...n 之間的數，加起來要最大，但有些數 banned 不能用。
// 先把 banned 變成 set() 方便快速查表，再用 for 迴圈「小到大」挑數字
class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        unordered_set<int> bannedSet; // 轉換成 Hash Set 讓之後的「比對」加快
        for(int b : banned) bannedSet.insert(b);
        int ans = 0, nowSum = 0;
        for(int i=1; i<=n; i++) {
            if(bannedSet.count(i) > 0) continue; // 「比對」到禁用的數，就換下一個
            if(nowSum+i > maxSum) break; // 加總超過範圍，就離開迴圈
            nowSum += i; // 沒事的話，加入此數
            ans++; // 答案 +1
        }
        return ans;
    }
};
