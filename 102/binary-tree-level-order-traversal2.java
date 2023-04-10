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
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        tree(root, 0);
        return ans;
    }
    void tree(TreeNode root, int level) {
        if(root==null) return;
        if(ans.size()<=level){
            ans.add(new ArrayList<Integer>());
        }
        List<Integer> now = ans.get(level);
        now.add(root.val);
        if(root.left!=null) tree(root.left, level+1);
        if(root.right!=null) tree(root.right, level+1);
    }
}
