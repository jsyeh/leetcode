/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int sumOfLeftLeaves2(struct TreeNode* root, bool left){
    if(root==NULL) return 0;
    if(left==true && root->left==NULL && root->right==NULL) return root->val;
    return sumOfLeftLeaves2(root->left, true) + sumOfLeftLeaves(root->right, false);

}
int sumOfLeftLeaves(struct TreeNode* root){
    if(root==NULL) return 0;
    
    return sumOfLeftLeaves2(root->left, true) + sumOfLeftLeaves2(root->right, false);
}
