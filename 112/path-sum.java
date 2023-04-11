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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null) return false;
        return leafHasPathSum(root, targetSum);
    }
    boolean leafHasPathSum(TreeNode root, int targetSum) {
        if(root==null && targetSum==0) return true;
        if(root==null && targetSum!=0) return false;
        if(root.right==null) return leafHasPathSum(root.left, targetSum-root.val);
        else if(root.left==null) return leafHasPathSum(root.right, targetSum-root.val);
        
        boolean b1 = leafHasPathSum(root.right, targetSum-root.val);
        boolean b2 = leafHasPathSum(root.left, targetSum-root.val);
        if(b1||b2) return true;
        else return false;
    }
}
