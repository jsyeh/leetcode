/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool LCA(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q, struct TreeNode** ans) {
    if(root==NULL) return false;
    bool center = (root==p || root==q);
    bool left = LCA(root->left, p, q, ans);
    bool right = LCA(root->right, p, q, ans);
    if( (left && right) || (left && center) || (right && center) ) {
        *ans = root;
//printf("root->val:%d\n", root->val);
    }
    return (left||right||center);    
}

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    struct TreeNode* ans;
    LCA(root, p, q, &ans);
    return ans;
}
