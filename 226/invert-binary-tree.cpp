// LeetCode 226. Invert Binary Tree 左右對調
class Solution {
public: // 已經有個函式, 寫好它, 就可「函式呼叫函式」
    TreeNode* invertTree(TreeNode* root) {
        if(root==nullptr) return root; // 終止條件
        TreeNode * left = invertTree(root->right); // 處理左邊的樹
        TreeNode * right = invertTree(root->left); // 處理右邊的樹
        root->left = left; // 將右邊放左邊
        root->right = right; // 將左邊放右邊
        return root;
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
