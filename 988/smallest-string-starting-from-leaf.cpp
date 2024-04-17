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
// 0..25 對應 'a'..'z'
// tree 的結構裡，要從 Leaf往上組字，找「對應比較小」的字串
// 因從下往上組字，所以需要走到 leaf 再進行比對。
// 因為 C 語言的字串處理, 手工管理要費很大的功夫, 所以老師用 C++ 的字串來示範
char table[] = "abcdefghijklmnopqrstuvwxyz"; //外面先用 C 的字元陣列(字串)做對照表
class Solution {
public:
    string helper(TreeNode* root, string nowStr) {
        // 現在的字串 nowStr 會慢慢變長
        if(root==nullptr) return nowStr; //走到最下面，回傳「累積的字串」
        // 左邊空，回傳右邊； 右邊空，回傳左邊
        if(root->left==nullptr) return helper(root->right, table[root->val]+ nowStr);
        if(root->right==nullptr) return helper(root->left, table[root->val] + nowStr);
        // 兩邊都有，回傳小的那個
        return min(helper(root->left, table[root->val]+nowStr), helper(root->right, table[root->val]+nowStr));

    }
    string smallestFromLeaf(TreeNode* root) {
        return helper(root, "");
    }
};
