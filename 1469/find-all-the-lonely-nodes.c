// lonely node 獨生子
// 關於tree的題目，大部分都用「函式呼叫函式」即可
// 但是要把「全部」的獨生子都回傳，需要準備正確的記憶體數量，比較麻煩
// 本來想 pass1 先數好「總量」，pass2再把答案放進去
// 後來發現，總共 1000個 node, 固定即可
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int ansN = 0;
int* ans = NULL;
void helper(struct TreeNode* root) { // 用來判斷「獨生子」並更新 ans 與 ansN
    if(root==NULL) return; // 沒有東西
    if(root->left==NULL && root->right!=NULL) { // 右邊的獨生子
        ans[ansN++] = root->right->val;
        helper(root->right);
    } else if(root->left!=NULL && root->right==NULL) { // 左邊的獨生子
        ans[ansN++] = root->left->val;
        helper(root->left);
    } else{ // 兩邊都有小孩，那就兩邊都繼續做下去
        helper(root->left);
        helper(root->right);
    }
}
int* getLonelyNodes(struct TreeNode* root, int* returnSize) {
    ansN = 0; // 因 LeetCode 會重覆呼叫函式，所以「要手動清為0」值才會正確
    if(ans==NULL) ans = (int*)malloc(sizeof(int)*1000); // 只要做一次，加速
    helper(root);
    *returnSize = ansN;
    return ans;
}
