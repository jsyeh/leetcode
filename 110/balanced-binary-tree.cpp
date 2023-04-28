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
    bool isBalanced(TreeNode* root) {
        int depth;
        bool ans = testDepth(root, depth);
        return ans;
    }
    bool testDepth(TreeNode* root, int & depth) {
        if(root==nullptr){
            depth=0;
            return true;
        }
        int left, right;
        if(!testDepth(root->left, left) || !testDepth(root->right, right)) return false;

        if(left>right) {
            if(left-right<=1) {
                depth = left+1;
                return true;
            } else {
                return false;
            }
        }else{
            if(right-left<=1) {
                depth = right+1;
                return true;
            } else {
                return false;
            }
        }
    }
};
