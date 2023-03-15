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
using namespace std;
class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        //solution: BFS, need queue, nothing null
        std::queue<TreeNode*> q;
        q.push(root);

        int state=1; // 1: non-nullptr, 每次有改變, 就 state++
        while(q.size()>0){
            TreeNode * now = q.front();
            if(now->left!=nullptr){
                q.push(now->left);
                if(state%2==0) state++;
            }else{
                if(state%2==1) state++;
            }
            if(now->right!=nullptr){
                q.push(now->right);
                if(state%2==0) state++;
            }else{
                if(state%2==1) state++;
            }
            q.pop();
        }
        if(state==2) return true;
        else return false;
    }
};
