/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSymmetric2(struct TreeNode * left, struct TreeNode * right){
    if(left==NULL && right==NULL) return true;
    if(left==NULL && right!=NULL) return false;
    if(left!=NULL && right==NULL) return false;
    if(left->val!=right->val) return false;

    return isSymmetric2(left->left, right->right) && isSymmetric2(left->right, right->left);
}
bool isSymmetric(struct TreeNode* root){
    if(root==NULL) return true;
    return isSymmetric2(root->left, root->right);
}
