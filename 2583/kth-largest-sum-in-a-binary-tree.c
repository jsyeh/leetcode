
// LeetCode 2583. Kth Largest Sum in a Binary Tree
// 找到「第k大」的 level sum (同一層的和)，可用「函式呼叫函式」可逐層分析
long long int levelSum[100000];  // 用來存每一層的 sum
int N = 0;
void helper(struct TreeNode* root, int level) {
    if(root==NULL) return; // 終止條件
    if(level>=N){ // 如果目前層數不夠
        levelSum[N++] = root->val; // 就新加1層
    } else { // 層數夠的話，就更新這層的「總合」
        levelSum[level] += root->val;
    }
    helper(root->left, level+1); // 函式呼叫函式
    helper(root->right, level+1); // 函式呼叫函式
}
int cmp(const void*p1, const void*p2) {
    long long int ans = *(long long int*)p1 - *(long long int*)p2;
    if(ans>0) return -1; // 全部從大到小排好
    else if(ans==0) return 0;
    else return 1;
}
long long kthLargestLevelSum(struct TreeNode* root, int k) {
    N = 0;  // 從新開始
    helper(root, 0); // 函式呼叫函式，從頭開始，往下處理
    qsort(levelSum, N, sizeof(long long), cmp);
    if(k>N) return -1; // 如果層數不夠，就 return -1 (k 是 1-index)
    else return levelSum[k-1]; // 找到第k大的數（改成 0-index）
}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
