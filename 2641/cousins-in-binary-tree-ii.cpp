// LeetCode 2641. Cousins in Binary Tree II
// 找出「有共同的祖先(但parent不同) 的堂兄弟姐妹「加起來」的值
// 看起來很難，但如果用昨天的 levelSum 技巧，找到同一層的sum，再減掉親兄弟sum即可
// 親兄弟sum，可暫存在parent裡面。之後再減掉它
class Solution {
public:
    vector<int> levelSum; //用來存「同一層的sum」
    int depth(TreeNode* root) {
        if(root==nullptr) return 0;
        return max(depth(root->left), depth(root->right)) + 1;
    }
    void helper(TreeNode* root, int level) {
        if(root==nullptr) return;
        levelSum[level] += root->val;
        helper(root->left, level+1);
        helper(root->right, level+1);
    }
    int helper2(TreeNode* root, int level) {
        if(root==nullptr) return 0;
        int myChildSum = helper2(root->left, level+1) + helper2(root->right, level+1);
        if(root->left != nullptr) root->left->val = levelSum[level+1] - myChildSum;
        if(root->right != nullptr) root->right->val = levelSum[level+1] - myChildSum;
        return root->val;
    }
    TreeNode* replaceValueInTree(TreeNode* root) {
        levelSum.resize(depth(root)); // 先調整陣列大小，以便加速
        helper(root, 0);
        helper2(root, 0);
        root->val = 0;
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
