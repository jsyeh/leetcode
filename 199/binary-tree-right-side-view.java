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
    List<Integer> right = new ArrayList<Integer>();
    public List<Integer> rightSideView(TreeNode root) {
        rightSideView(root, 0);
        return right;
    }
    void rightSideView(TreeNode root, int level) {
        if(root==null) return;
        if(right.size()<=level) right.add(root.val);
        else right.set(level, root.val);
        rightSideView(root.left, level+1);
        rightSideView(root.right, level+1);
    }
}
