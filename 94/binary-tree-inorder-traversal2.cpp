// LeetCode 94. Binary Tree Inorder Traversal
class Solution {
public:
    void helper(TreeNode* root, vector<int>& ans) { // 函式呼叫函式
        if(root==nullptr) return; // 終止條件、結束條件 terminal condition

        helper(root->left, ans); // 左半邊
        ans.push_back(root->val); // 塞在中間
        helper(root->right, ans); // 右半邊
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans; // 準備 ans 答案 (伸縮自如的陣列)
        helper(root, ans); // 函式呼叫函式 幫我們把答案算出來,塞入ans
        return ans; // ans 答案丟出去
    }
};
