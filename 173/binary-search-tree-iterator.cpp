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
class BSTIterator {
public:
    stack<int> data;
    BSTIterator(TreeNode* root) {
        buildStack(root);
    }
    void buildStack(TreeNode* root){
        if(root->right!=nullptr) buildStack(root->right);
        data.push(root->val);
        if(root->left!=nullptr) buildStack(root->left);
    }
    
    int next() {
        if(data.size()==0) return 0;
        int ans = data.top();
        data.pop();
        return ans;
    }
    
    bool hasNext() {
        return data.size()>0;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
