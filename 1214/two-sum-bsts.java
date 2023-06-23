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
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        HashSet<Integer> tree1 = new HashSet<>();
        visiting(root1, tree1);

        return checking(root2, tree1, target);
    }
    void visiting(TreeNode root1, HashSet<Integer> tree1) {
        if(root1==null) return;
        tree1.add(root1.val);
        visiting(root1.left, tree1);
        visiting(root1.right, tree1);
    }
    boolean checking(TreeNode root2, HashSet<Integer> tree1, int target) {
        if(root2==null) return false;
        if(tree1.contains(target-root2.val)) return true;

        return checking(root2.left, tree1, target) || checking(root2.right, tree1, target);
    }
}
