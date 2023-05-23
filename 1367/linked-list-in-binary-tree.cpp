/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
//這裡的解法, 我參考了 lee215 的解法, 實在有夠帥
//https://leetcode.com/problems/linked-list-in-binary-tree/solutions/524881/python-recursive-solution-o-n-l-time/
    bool isSubPath(ListNode* head, TreeNode* root) {
        if(head==nullptr) return true; //就當是比完、成功了
        if(root==nullptr) return false;//前一行沒離開,結果root沒資料,就沒辦法比下去了

        return dfs(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
        //   以root開始逐一比對    請下一代再去找吧
    }
    bool dfs(ListNode * head, TreeNode* root) {
        if(head==nullptr) return true;
        if(root==nullptr) return false;//這兩行, 同 isSubPath() 的前兩行

        if(head->val != root->val) return false; //不相同, 提早結束
        else return dfs(head->next, root->left) || dfs(head->next, root->right);
    }
};
