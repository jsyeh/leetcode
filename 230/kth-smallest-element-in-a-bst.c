/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool find(struct TreeNode* root, int *k, int *ans){
    if(root==NULL) return false;
    if(find(root->left, k, ans)==true) return true;
    (*k)--;
    if(*k==0){
        *ans = root->val;
        return true;
    }
    find(root->right, k, ans);
    if(*k>0) return false;
    else return true;
}
int kthSmallest(struct TreeNode* root, int k){
    int ans;
    find(root, &k, &ans);
    return ans;
}
