// LeetCode 2107. Number of Unique Flavors After Sharing K Candies
// candies[i] 是口味，把「連續k個糖果」給妹妹後，自己最多有幾種「不同口味」的糖果
// 可利用 sliding window 來解決這題
class Solution {
public:
    int shareCandies(vector<int>& candies, int k) {
        map<int,int> counter; // 用 Counter()快速知道有幾種「不同口味」的糖果
        int N = candies.size();
        int unique = 0;
        for(int i=k; i<N; i++) { // 「最前面k個」給妹妹，統計「k後面」的糖果
            int now = candies[i];
            if(counter[now]==0) unique++;
            counter[now]++; // 這個口味的糖果數量增加
        }
        int ans = unique;
        for(int i=0; i<N-k; i++) { // 開始滑動
            int now = candies[i], now2 = candies[k+i];
            if(counter[now]==0) unique++; // 若增加前是0，就+1
            counter[now]++; // 左邊還回來
            counter[now2]--; // 右邊送出去
            if(counter[now2]==0) unique--; // 若減少後變0，就-1
            ans = max(ans, unique); // 更新答案
        }
        return ans;
    }
};

