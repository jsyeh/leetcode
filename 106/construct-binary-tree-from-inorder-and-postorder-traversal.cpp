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
    map<int, int> mapIn; //In-order
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int N = inorder.size();
        for(int i=0; i<N; i++){
            mapIn.insert( pair<int,int>(inorder[i], i) );
        }
        
        TreeNode * ans = myBuildTree(inorder, 0, N-1, postorder, 0, N-1); 
        return ans;
    }
    TreeNode* myBuildTree(vector<int>& inorder, int inLeft, int inRight, vector<int>& postorder, int postLeft, int postRight){
        if(inLeft>inRight) return nullptr;
        if(inLeft==inRight) return new TreeNode(inorder[inLeft]);
        int rootVal = postorder[postRight];
        int rootPos = mapIn.at(rootVal);
        int postCenter = postLeft + (rootPos-1-inLeft);

        TreeNode * now = new TreeNode(rootVal);

        now->left = myBuildTree(inorder, inLeft, rootPos-1, postorder, postLeft, postCenter);
        now->right = myBuildTree(inorder, rootPos+1, inRight, postorder, postCenter+1, postRight-1);
        return now;
    }
};
