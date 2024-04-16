/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// 要將 tree 的 node tilt的總合，也就是全部的abs(左樹總和-右樹總和)
// tree本身的值，會變成它的 children 的差
int ans = 0;
int helper(struct TreeNode* root) { // 會回傳「此樹的加總」 同時會把abs()答案加到 ans 裡
    if(root==NULL) return 0;
    int left = helper(root->left);
    int right = helper(root->right);
    ans += abs(left-right); // 同時會把答案加到 ans 裡
    return left + right + root->val;
}
int findTilt(struct TreeNode* root) {
    ans = 0; // 每次都要手動清為0
    helper(root); // 計算加總，並把tilt abs()答案累積到 self.ans
    return ans;
}
