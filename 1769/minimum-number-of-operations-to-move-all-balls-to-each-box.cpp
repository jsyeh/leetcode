// LeetCode 1769. Minimum Number of Operations to Move All Balls to Each Box
// 字串 boxes 對應 n 個盒子（0空的、1有球）。若想分別「將球集中」在某個盒子，要分別移動幾步呢？
// 因盒子較少1000個，真的用暴力法，也能及時算完。
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int N = boxes.length(); // 有 N 個盒子
        vector<int> ans(N); // 放答案的陣列
        for(int i=0; i<N; i++) { // 針對 box i
            int now = 0; // 累積 box i 對應的答案
            for(int j=0; j<N; j++) { // 巡視 box j
                if(boxes[j]=='1') now += abs(i-j); // 若有球，就更新答案
            }
            ans[i] = now; // 把答案放入 ans[i]
        }
        return ans;
    }
};
