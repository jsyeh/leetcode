/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int bad = 0;
int height(struct TreeNode* root){
    if(root==NULL) return 0;
    int h1 = height(root->left);
    int h2 = height(root->right);
    if(!(h1==h2 || h1+1==h2 || h1==h2+1)) bad = 1;
    
    if(h1>h2) return h1 + 1;
    else return h2 + 1;
}
bool isBalanced(struct TreeNode* root){
    if(root==NULL) return true;

    bad = 0;
    height(root);
    if(bad==0) return true;
    else return false;
}
