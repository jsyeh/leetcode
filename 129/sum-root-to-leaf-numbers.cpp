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
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        int sum = 0;
        return allChildrenValue(root, 0);
    }
    int allChildrenValue(TreeNode* now, int parentValue) {
        int nowValue = parentValue*10+now->val;
        if(now->left==nullptr && now->right==nullptr) return nowValue;
        if(now->left==nullptr) return allChildrenValue(now->right, nowValue);
        if(now->right==nullptr) return allChildrenValue(now->left, nowValue);
        return allChildrenValue(now->left, nowValue) + allChildrenValue(now->right, nowValue);
    }
};
