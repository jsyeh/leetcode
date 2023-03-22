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
    //Idea: BFS
    List<List<Integer>> ans;
    public List<List<Integer>> levelOrder(TreeNode root) {
        ans = new LinkedList<List<Integer>>();
        levelOrder(root, 0);
        return ans;
    }
    void levelOrder(TreeNode root, int level) {
        if(root==null) return;

        if(ans.size()<=level){
            ans.add(new LinkedList<Integer>());
        }

        List<Integer> current = ans.get(level);
        current.add(root.val);
        if(root.left!=null){
            levelOrder(root.left, level+1);
        }
        if(root.right!=null){
            levelOrder(root.right, level+1);
        }
    }
}
