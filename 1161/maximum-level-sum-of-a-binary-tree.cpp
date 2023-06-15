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
    vector<int> sum;
    int maxLevelSum(TreeNode* root) {
        sum.push_back(0);
        helper(root, 1);
        int maxI = 1;
        for(int i=1; i<sum.size(); i++){
            if(sum[i]>sum[maxI]) maxI = i;
        }
        return maxI;
    }
    void helper(TreeNode* root, int level) {
        if(root==nullptr) return;

        if(sum.size()<=level) {
            sum.push_back(root->val);
        }else sum[level]+=root->val;

        if(root->left!=nullptr) helper(root->left, level+1);
        if(root->right!=nullptr) helper(root->right, level+1);
    }
};
//case 38/40: [-100,-200,-300,-20,-5,-10,null]
