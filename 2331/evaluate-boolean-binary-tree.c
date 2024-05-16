/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// LeetCode 2331. Evaluate Boolean Binary Tree
// 樹的 leaf: 0:False, 1:True
// 其他 node: 2:OR, 3:AND
// 想要模擬結果，就照著規則模擬即可
bool evaluateTree(struct TreeNode* root) {
    if(root->left==NULL && root->right==NULL) { // leaf node 端點的葉子
        return root->val == 1;  // 1就True, 0就False
    } else if(root->val == 2) {  // 接下來，就是 non-leaf node, 進行 OR 運算
        return evaluateTree(root->left) || evaluateTree(root->right);
    } else { // 進行 AND 運算
        return evaluateTree(root->left) && evaluateTree(root->right);
    }
}
