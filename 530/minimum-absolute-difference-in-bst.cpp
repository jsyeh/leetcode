/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        //因為 BST tree, 所以其實能找到全部相鄰的數。接著便能找到全部的(兩數間)差距,找到最小的差距離
        long long prev = INT_MIN;//最小的數
        long long ans = INT_MAX;
        helper(root, &prev, &ans);
        return ans;
    }
    void helper(TreeNode* root, long long * prev, long long * ans){
        if(root==nullptr) return;

        helper(root->left, prev, ans);

        long long temp = root->val - *prev;
        if(temp<*ans) *ans = temp;
        *prev = root->val;
//printf("%lld (ans:%lld) ", *prev, *ans);
        helper(root->right, prev, ans);
    }
};
