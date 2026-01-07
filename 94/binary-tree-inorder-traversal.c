// LeetCode 94. Binary Tree Inorder Traversal
// 將 binary tree 的每個值，都順利填入
int N = 0;
int * ans = NULL;
int treeSize(struct TreeNode* root) { // 先知 Tree 的大小，才能準備 memory
    if (root==NULL) return 0;
    return treeSize(root->left) + treeSize(root->right) + 1;
}
void fillValue(struct TreeNode* root) {
    if (root==NULL) return;
    fillValue(root->left);
    printf("now N:%d\n", N);
    ans[N++] = root->val;
    fillValue(root->right);
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = treeSize(root);
    ans = (int*) malloc(sizeof(int)*(*returnSize)); // global 變數
    N = 0;
    fillValue(root);
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
