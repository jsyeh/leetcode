// 要找到 tree 裡「第2小的數」
// (1) 解法應該是「先找最小的數」，同時就會更新「第2小的數」
// 不過題目有個有趣的限制：root一定是最小的數
// (2) 另一種解法，是「只要與 root 不同，就是「第2小的數」
// 可惜，在 case 37/39 發現這個方法不對。還是用方法1吧！
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int small1, small2;
void helper(struct TreeNode* root) {
    if(small1==-1 || root->val<small1) {
        small2 = small1;
        small1 = root->val;
    }else if(root->val!=small1 && (small2==-1 || root->val<small2)) {
        small2 = root->val;
    }
    if(root->left!=NULL) helper(root->left);
    if(root->right!=NULL) helper(root->right);
}
int findSecondMinimumValue(struct TreeNode* root) {
    small1 = -1;
    small2 = -1;
    helper(root);
    return small2;
}
// case 37/39: [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]
