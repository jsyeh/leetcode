//把root走到leaf的數值，全部加起來，簡單「函式呼叫函式」即可！
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int pathSum(struct TreeNode* root, int prev) { // 幫忙算出root到leaf的10進位的值
    if(root==NULL) return 0; // 空指標，就沒東西
    if(root->left==NULL && root->right==NULL) { // 葉子節點
        return prev*10 + root->val; // 就把累積的數字 return
    }
    // 函式呼叫函式，回傳 左樹的結果 + 右樹的結果
    return pathSum(root->left, prev*10 + root->val) + pathSum(root->right, prev*10 + root->val);
}
int sumNumbers(struct TreeNode* root) {
    return pathSum(root, 0);
}
