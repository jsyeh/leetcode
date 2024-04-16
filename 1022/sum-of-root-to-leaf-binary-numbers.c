// 從 root 到 leaf 以「二進位」來表現
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int helper(struct TreeNode* root, int prev) { // 幫忙「函式呼叫函式」處理。prev 記錄之前走過的2進位數
    if(root==NULL) return 0; // 空指標，不處理
    int now = prev*2 + root->val;
    if(root->left==NULL && root->right==NULL) return now; // 遇到葉子，才回傳
    return helper(root->left, now) + helper(root->right, now); // 不是葉子，就繼續
}
int sumRootToLeaf(struct TreeNode* root) {
    return helper(root, 0);
}
