// LeetCode 1769. Minimum Number of Operations to Move All Balls to Each Box
// 字串 boxes 對應 n 個盒子（0空的、1有球）。若想分別「將球集中」在某個盒子，要分別移動幾步呢？
// 因盒子較少1000個，真的用暴力法，也能及時算完。但想更「優美、有效率」解決，可使用 prefix 技巧
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int N = boxes.length(); // 有 N 個盒子
        vector<int> ans(N), prefix(N+1), postfix(N+1);
        int left = 0, right = 0;
        for(int i=0; i<N; i++) {
            prefix[i+1] = prefix[i] + left;
            if(boxes[i]=='1') {
                left++;
                prefix[i+1]++;
            }
            postfix[N-1-i] = postfix[N-i] + right;
            if(boxes[N-1-i]=='1') {
                right++;
                postfix[N-1-i]++;
            }
        }
        for(int i=0; i<N; i++) {
            ans[i] = prefix[i] + postfix[i+1];
        }
        return ans;
    }
};
