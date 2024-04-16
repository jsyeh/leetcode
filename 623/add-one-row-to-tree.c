// 要將某個數字val，插入tree的第depth行
// 應該還是「函式呼叫函式」來解
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* newTreeNode(int val, struct TreeNode* left, struct TreeNode* right) {
    struct TreeNode* root2 = (struct TreeNode*) malloc(sizeof(struct TreeNode));
    root2->val = val;
    root2->left = left;
    root2->right = right;
    return root2;
}
struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth) {
    if(root==NULL) return NULL;
    if(depth==1) { // 特殊狀況，要新建更上面一層
        root = newTreeNode(val, root, NULL); // 把舊的接在左邊
    } else if(depth==2) { // 下面要先插入val，再往下接
        root->left = newTreeNode(val, root->left, NULL);
        root->right = newTreeNode(val, NULL, root->right);
    } else { // 層數還沒到，就再往下「函式呼叫函式」
        addOneRow(root->left, val, depth-1);
        addOneRow(root->right, val, depth-1);
    }
    return root;
}
