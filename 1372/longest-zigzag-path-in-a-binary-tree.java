/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int longestZigZag(TreeNode root) {
        return dfs(root)[2];
    }
    int[] dfs(TreeNode root) {
        if(root==null) return new int[]{-1, -1, -1};// 所以最下面的真的點會得到0,因為會再+1

        int [] leftChild = dfs(root.left);
        int [] rightChild = dfs(root.right);
        int leftAns = leftChild[1] + 1;
        int rightAns = rightChild[0] + 1;
        int maxAns = max(leftChild[2], rightChild[2]);
        if(leftAns>maxAns) maxAns = leftAns;
        if(rightAns>maxAns) maxAns = rightAns;
        return new int[]{leftAns, rightAns, maxAns};
    }
    int max(int a, int b){
        if(a>b) return a;
        else return b;
    }
}
