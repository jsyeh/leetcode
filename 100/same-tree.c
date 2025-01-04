// LeetCode 100. Same Tree
// 看兩棵樹是否「完全相同」
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if(p==NULL && q==NULL) return true; // 都是空的，一樣
    if(p==NULL || q==NULL) return false; // 只有一邊是空的，失敗
    if(p->val != q->val) return false; // 不同，失敗
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
