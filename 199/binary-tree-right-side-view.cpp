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
    vector<int> ans;
    vector<int> rightSideView(TreeNode* root) {
        rightSideView(root, 0);
        return ans;
    }
    void rightSideView(TreeNode* root, int level) {
        if(root==nullptr) return;

        if(level>=ans.size()){
            ans.push_back(root->val);
        }else{
            ans[level] = root->val;
        }
        rightSideView(root->left, level+1);
        rightSideView(root->right, level+1);
    }
};
