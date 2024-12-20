// LeetCode 2415. Reverse Odd Levels of Binary Tree
// tree 是完整的，裡面奇數層要左右對調。用「函式呼叫函式」應可解決
class Solution {
public:
    void buildOddLevel(TreeNode* root, int level, vector<stack<int>>& oddLevel) {
        if(root==nullptr) return; // 終止條件
        if(oddLevel.size()<=level/2) { // 層數不夠，就加
            oddLevel.push_back( stack<int>() );
        }
        if(level%2==1) { // 這裡用 oddLevel[level/2] 對應 level 層，省一半空間
            oddLevel[level/2].push(root->val);
        }
        buildOddLevel(root->left, level+1, oddLevel); // 函式呼叫函式、左半邊
        buildOddLevel(root->right, level+1, oddLevel); // 函式呼叫函式、右半邊
    }
    void changeOddLevel(TreeNode* root, int level, vector<stack<int>>& oddLevel) {
        if(root==nullptr) return;
        if(level%2==1) {
            root->val = oddLevel[level/2].top(); // 利用 stack 先進後出、後進先出，來reverse
            oddLevel[level/2].pop(); // 用掉，就吐掉
        }
        changeOddLevel(root->left, level+1, oddLevel); // 函式呼叫函式、左半邊
        changeOddLevel(root->right, level+1, oddLevel); // 函式呼叫函式、右半邊
    }
    TreeNode* reverseOddLevels(TreeNode* root) {
        vector<stack<int>> oddLevel;
        buildOddLevel(root, 0, oddLevel);
        changeOddLevel(root, 0, oddLevel);
        return root;
    }
};
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

