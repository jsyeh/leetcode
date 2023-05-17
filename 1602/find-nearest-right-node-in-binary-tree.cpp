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
    TreeNode* findNearestRightNode(TreeNode* root, TreeNode* u) {
        int state = 0; //0: finding, 1: found u, 2; next in same level
        int targetLevel = 0;
        return travel(root, u, state, 0, targetLevel);
    }
    TreeNode* travel(TreeNode* root, TreeNode* u, int& state, int level, int& targetLevel){
        if(state==0 && root==u){
            state=1;
            targetLevel = level;
            return nullptr;
        }
        if(state==1 && level== targetLevel && root!=nullptr){
            state=2;
            return root;
        }

        if(root==nullptr) return root;

        TreeNode* left = travel(root->left, u, state, level+1, targetLevel);
        if(left!=nullptr) return left;

        return travel(root->right, u, state, level+1, targetLevel);
    }
};
//case 59/76: [17,14,5,null,7,null,12,3,null,9,19,10,13,null,18,24,21,22,null,null,null,null,null,20,null,23,8,15,6,null,null,1,4,null,null,null,null,null,null,2,null,11,null,16] 3
