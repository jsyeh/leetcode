// LeetCode 104. Maximum Depth of Binary Tree
class Solution {
public:
    // Binary Tree 最喜歡用「函式呼叫函式」來解
    // 英文 Recursion(遞迴) 或 Recursive Function Call
    int maxDepth(TreeNode* root) {
        if (root==nullptr) return 0; // 終止條件 什麼都沒有
        int left = maxDepth(root->left); // 函式呼叫函式
        int right = maxDepth(root->right); // 函式呼叫函式
        return max(left, right) + 1; // 再加1層樓
    }
};
