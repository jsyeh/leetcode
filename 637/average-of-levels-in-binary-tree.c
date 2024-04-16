// 計算「每一層」總和後的平均
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
double* ans = NULL;
int* count = NULL;
void helper(struct TreeNode* root, int level) { // 用 helper 來累積 ans
    if(root==NULL) return; // 結束
    if(ansN<=level) { // 還差這一層
        count[ansN] = 1;
        ans[ansN++] = root->val;
    } else { // 已經有這一層
        count[level] ++;
        ans[level] += root->val;
    }
    helper(root->left, level+1);
    helper(root->right, level+1);
}
double* averageOfLevels(struct TreeNode* root, int* returnSize) {
    ansN = 0;
    if(ans==NULL) ans = (double*) malloc(sizeof(double)*10000); //再動態清為0即可
    if(count==NULL) count = (int*) malloc(sizeof(int)*10000); //再動態清為0即可
    helper(root, 0);
    for(int i=0; i<ansN; i++) {
        ans[i] = ans[i] / count[i]; //計算平均
    }
    *returnSize = ansN;
    return ans;
}
