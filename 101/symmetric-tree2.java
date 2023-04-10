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
    public boolean isSymmetric(TreeNode root) {
        return isSymmetric(root.left, root.right);
    }
    boolean isSymmetric(TreeNode left, TreeNode right) {
        if(left==right) return true;
        if(left==null || right==null) return false;
        if(left.val!=right.val) return false;
        if(isSymmetric(left.left, right.right)==false) return false;
        if(isSymmetric(left.right, right.left)==false) return false;
        return true;
    }
}
