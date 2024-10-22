// LeetCode 2583. Kth Largest Sum in a Binary Tree
// 找到「第k大」的 level sum (同一層的和)，可用「函式呼叫函式」可逐層分析
class Solution {
public:
    vector<long long> levelSum; // 用來存每一層的 sum
    void helper(TreeNode* root, int level) {
        if(root==nullptr) return; // 終止條件
        if(levelSum.size()<=level) { // 如果目前層數不夠
            levelSum.push_back(root->val); // 就新加1層
        } else { // 層數夠的話，就更新這層的「總合」
            levelSum[level] += root->val;
        }
        helper(root->left, level+1); // 函式呼叫函式
        helper(root->right, level+1);
    }
    long long kthLargestLevelSum(TreeNode* root, int k) {
        helper(root, 0); // 函式呼叫函式，從頭開始，往下處理

        if(k>levelSum.size()) return -1; // 如果層數不夠，就 return -1 (k 是 1-index)
        sort(levelSum.begin(), levelSum.end());
        return levelSum[levelSum.size() - k]; // 找到第k大的數（改成 0-index）
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
