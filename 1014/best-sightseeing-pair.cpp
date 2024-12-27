// LeetCode 1014. Best Sightseeing Pair
// 每個景點的價值 values[i], 挑2個景點，希望景點「價值高」，又希望兩個景點「距離近」，
// 目標是 values[i] + values[j] - (距離) 最大，即 values[i] +values[j] - abs(j-i) 最大
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int prevBest = values[0], ans = 0;
        for(int i=1; i<values.size(); i++) {
            ans = max(ans, prevBest + values[i] - 1);
            prevBest = max(prevBest-1, values[i]);
        }
        return ans;
    }
};
