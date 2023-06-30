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
    int revl;//這個變數，用來暫存「剛剛呼叫的函式，下面有多少個 uni-value subtree 的答案
    int countUnivalSubtrees(TreeNode* root) {
        if(root==nullptr) return 0; //空指標，不要去呼叫

        helper(root);
        return revl;
    }
    int helper(TreeNode* root) { //這裡return 的值，是uni-value
        if(root==nullptr) { //因為設計得巧妙，希望進來的都不是 nullptr （這段只是寫好心安的）
            revl = 0;
            return 0;
        }
        if(root->left==nullptr && root->right==nullptr) {
            revl = 1; //本身就是一個 uni-value subtree
            return root->val;
        }

        int temp1=0, temp2=0; //用來拉 revl 的值
        int uni_1=INT_MAX, uni_2=INT_MAX; ///INT_MAX:沒動過，INT_MIN:沒有uni-value
        if(root->left!=nullptr) {
            uni_1 = helper(root->left);
            temp1 = revl;
        }
        if(root->right!=nullptr) {
            uni_2 = helper(root->right);
            temp2 = revl;
        }
        revl = temp1 + temp2;
        if(uni_1==INT_MIN) return INT_MIN; //沒有uni-value
        if(uni_2==INT_MIN) return INT_MIN; //沒有uni-value

        //最後，要判斷 uni-value 是什麼
        if(root->left==nullptr) {
            if(uni_2==root->val) {
                revl++;
                return root->val;//找到 uni-value
            } else return INT_MIN;
        } else if(root->right==nullptr) {
            if(uni_1==root->val) {
                revl++;
                return root->val;//找到 uni-value
            } else return INT_MIN;
        } else {
            if(uni_1 == uni_2 && uni_2 == root->val) {
                revl++;
                return root->val;//找到 uni-value
            } else return INT_MIN;
        }

    }
};
