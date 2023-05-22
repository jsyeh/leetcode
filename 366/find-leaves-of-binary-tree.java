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
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        while(root!=null) {
            List<Integer> temp = new ArrayList<Integer>();
            ans.add(findLeaves(root, temp));
            root = removeLeaves(root);
System.out.println();
        }
        return ans;
    }
    List<Integer> findLeaves(TreeNode root, List<Integer> ans) {
        if(root==null) return ans;
        if(root.left==null && root.right==null) {
System.out.print(root.val + " ");
            ans.add(root.val);
            return ans;
        }
        findLeaves(root.left, ans);
        findLeaves(root.right, ans);
        return ans;
    }
    TreeNode removeLeaves(TreeNode root) {
        if(root==null) return root;
        if(root.left==null && root.right==null) return null;
        root.left = removeLeaves(root.left);
        root.right = removeLeaves(root.right);
        return root;
    }
}
