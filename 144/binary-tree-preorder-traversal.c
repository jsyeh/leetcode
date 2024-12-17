// LeetCode 144. Binary Tree Preorder Traversal
// 將 tree 以 preorder 的方式走訪，也就是「中間」先，再左邊、再右邊
int countHelper(struct TreeNode* root) {
    if(root==NULL) return 0;
    return countHelper(root->left) + countHelper(root->right) + 1;
}
int * ans;
int ansN = 0;
void helper(struct TreeNode* root) {
    if(root==NULL) return;
    ans[ansN++] = root->val;
    helper(root->left);
    helper(root->right);
}
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    int N = countHelper(root);
    ans = (int*) malloc(sizeof(int)*N);
    ansN = 0;
    helper(root);
    *returnSize = N;
    return ans;
}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

