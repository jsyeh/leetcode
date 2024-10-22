// LeetCode 2583. Kth Largest Sum in a Binary Tree
// 找到「第k大」的 level sum (同一層的和)，可用「函式呼叫函式」可逐層分析
class Solution {
public:
    vector<long long> levelSum; // 用來存每一層的 sum
    int depth(TreeNode* root) {
        if(root==nullptr) return 0;
        return max(depth(root->left), depth(root->right)) + 1;
    }
    void helper(TreeNode* root, int level) {
        if(root==nullptr) return; // 終止條件
        //if(levelSum.size()<=level) { // 如果目前層數不夠
        //    levelSum.push_back(root->val); // 就新加1層（有可能是這裡太慢）
        //} else { // 層數夠的話，就更新這層的「總合」
        //    levelSum[level] += root->val;
        //}
        
        levelSum[level] += root->val; // 先 resize(depth) 後，就不用 push_back()

        helper(root->left, level+1); // 函式呼叫函式
        helper(root->right, level+1);
    }
    long long kthLargestLevelSum(TreeNode* root, int k) {
        levelSum.resize(depth(root)); 
        // 用 resize(depth) 避免 push_back()，上傳後加速，變 17 ms

        helper(root, 0); // 函式呼叫函式，從頭開始，往下處理

        if(k>levelSum.size()) return -1; // 如果層數不夠，就 return -1 (k 是 1-index)
        //sort(levelSum.begin(), levelSum.end()); // 用 sort()太慢了，耗時 823 ms
        //return levelSum[levelSum.size() - k]; // 找到第k大的數（改成 0-index）
        priority_queue<long long> pq(levelSum.begin(), levelSum.end());
        for(int i=0; i<k-1; i++){ // 改用 priority_queue 來加速，把k-1項大的丟掉
            pq.pop(); //但還是很慢，耗時 819 ms
        }
        return pq.top(); // 最後剩下答案
    }
};
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
