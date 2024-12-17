// LeetCode 144. Binary Tree Preorder Traversal
// 將 tree 以 preorder 的方式走訪，也就是「中間」先，再左邊、再右邊
class Solution {
public:
    void helper(TreeNode* root, vector<int>& ans) {
        if(root==nullptr) return;
        ans.push_back(root->val);
        helper(root->left, ans);
        helper(root->right, ans);
    }
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        helper(root, ans);
        return ans;
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
