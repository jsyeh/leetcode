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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<Integer> list = new ArrayList<Integer>();
        pathSum(root, targetSum, list);
        return ans;
    }
    void pathSum(TreeNode root, int targetSum, List<Integer> list) {
        if(root==null) return;
        if(root.left==null && root.right==null && root.val == targetSum) {
            List<Integer> temp = new ArrayList<Integer>(list);
            temp.add(root.val);
            ans.add(temp);
            return;
        }

        List<Integer> temp = new ArrayList<Integer>(list);
        temp.add(root.val);
        if(root.left!=null) pathSum(root.left, targetSum-root.val, temp);
        if(root.right!=null) pathSum(root.right, targetSum-root.val, temp);
    }
}
