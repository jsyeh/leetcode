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
    public boolean isValidBST(TreeNode root) {
        //return isValidBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        //不能使用 Integer.MIN_VALUE 及 Integer.MAX_VALUE,因 Node.val 可能碰到
        return isValidBST(root, null, null);
    }
    //boolean isValidBST(TreeNode root, int left, int right) {
    boolean isValidBST(TreeNode root, Integer left, Integer right) {
        if(root==null) return true;
        //萬用的 null 遇到的話，就算通過
        if( (left==null || left<root.val) && (right==null || root.val<right) ){
        //if( left<root.val && root.val<right ){
            if(root.left==null || (root.left!=null && isValidBST(root.left, left, root.val)) ){
                //good
            }else return false;
            if(root.right==null || (root.right!=null && isValidBST(root.right, root.val, right))){
                //good
            }else return false;
            return true;
        } else return false;
    }
}
