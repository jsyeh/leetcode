// LeetCode 1644. Lowest Common Ancestor of a Binary Tree II
// 想找出 TreeNode p 和 TreeNode q 的共同祖先
class Solution {
public:
    TreeNode* ans;
    int helper(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==nullptr) return 0;
        int count = (root==p || root==q) ? 1 : 0;
        int count1 = helper(root->left, p, q);
        if(count1==2) return 2; // 左邊有答案
        int count2 = helper(root->right, p, q);
        if(count2==2) return 2; // 右邊有咎案
        if(count+count1+count2==2) ans = root; // 現在剛好找到答案
        return count+count1+count2;
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        ans = nullptr;
        if(helper(root, p, q)==2) return ans;
        return nullptr;
    }
};
