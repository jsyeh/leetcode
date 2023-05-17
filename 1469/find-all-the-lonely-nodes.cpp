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
    vector<int> getLonelyNodes(TreeNode* root) {
        vector<int> ans;
        travel(root, ans);
        return ans;
    }
    void travel(TreeNode * root, vector<int>&ans) {
        if(root==nullptr) return;

        if(root->left != nullptr && root->right == nullptr) {
            ans.push_back(root->left->val);
            travel(root->left, ans);
        }else if(root->right != nullptr && root->left == nullptr) {
            ans.push_back(root->right->val);
            travel(root->right, ans);
        }else{
            travel(root->left, ans);
            travel(root->right, ans);
        }
    }
};
