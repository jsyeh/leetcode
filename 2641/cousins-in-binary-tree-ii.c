// LeetCode 2641. Cousins in Binary Tree II
// 找出「有共同的祖先(但parent不同) 的堂兄弟姐妹「加起來」的值
// 看起來很難，但如果用昨天的 levelSum 技巧，找到同一層的sum，再減掉親兄弟sum即可
// 親兄弟sum，可暫存在parent裡面。之後再減掉它
int levelSum[100000];
int max(int a, int b) {
    if(a>b) return a;
    else return b;
}
int depth(struct TreeNode* root) {
    if(root==NULL) return 0;
    return max(depth(root->left), depth(root->right)) + 1;
}
void helper(struct TreeNode* root, int level) {
    if(root==NULL) return;
    levelSum[level] += root->val;
    helper(root->left, level+1);
    helper(root->right, level+1);
}
int helper2(struct TreeNode* root, int level) {
    if(root==NULL) return 0;
    int childSum = helper2(root->left, level+1) + helper2(root->right, level+1);
    if(root->left) root->left->val = levelSum[level+1] - childSum;
    if(root->right) root->right->val = levelSum[level+1] - childSum;
    return root->val;
}
struct TreeNode* replaceValueInTree(struct TreeNode* root) {
    int levelN = depth(root);
    for(int i=0; i<levelN; i++) levelSum[i] = 0;
    helper(root, 0);
    helper2(root, 0);
    root->val = 0;
    return root;
}

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

