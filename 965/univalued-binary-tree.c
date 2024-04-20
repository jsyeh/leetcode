// 想確認tree裡每個node的值都相同，就用 verifyAll 配上val值來檢查
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool verifyAll(struct TreeNode* root, int val) { // 是否值符合？
    if(root==NULL) return true; // 順利走到結束
    if(root->val != val) return false; // 遇到不相同
    return verifyAll(root->left, val) && verifyAll(root->right, val);
    // 是否左右都同時符合？
}
bool isUnivalTree(struct TreeNode* root) {
    return verifyAll(root, root->val);
}
