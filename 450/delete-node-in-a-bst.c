/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int findLeftMost(struct TreeNode* root){
    if(root->left!=NULL) return findLeftMost(root->left);
    else return root->val;
}
//需要 findLeftMost() 及 findRightMode()
//但這又可能造成下面的 node 又要再 delete 的狀況
struct TreeNode* deleteNode(struct TreeNode* root, int key){
    if(root==NULL) return root;
    if(root->val==key) {
        if(root->left==NULL && root->right==NULL) return NULL;
        if(root->right!=NULL && root->left==NULL) return root->right;
        if(root->left!=NULL && root->right==NULL) return root->left;
        root->val = findLeftMost(root->right);
        root->right = deleteNode(root->right, root->val);
        return root;
    }//不能直接上搬，因為會犧牲另一邊的sub-tree

    root->left = deleteNode(root->left, key);
    root->right = deleteNode(root->right, key);
    return root;
}
