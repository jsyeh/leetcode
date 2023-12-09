// 這題是簡單的 Tree Traversal 走訪的題目
// 只要利用「函式呼叫函式」的方式，配合前面先有「終止條件」便能完成
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans; // 準備好可回傳的資料結構
        if(root==nullptr) return ans; //終止條件，回傳空的 vector

        vector<int> left = inorderTraversal(root->left); //左半樹
        vector<int> right = inorderTraversal(root->right); //右半樹
        ans.insert(ans.end(), left.begin(), left.end() ); //先左
        ans.push_back(root->val); //再中間
        ans.insert(ans.end(), right.begin(), right.end() ); //再右
        return ans;
    }
};
