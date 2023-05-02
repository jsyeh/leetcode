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
class BSTIterator {
    Stack<Integer> stack = new Stack<Integer>();
    public BSTIterator(TreeNode root) {
        buildStack(root);
    }
    void buildStack(TreeNode root) {
        if(root==null) return;
        if(root.right!=null) buildStack(root.right);
        stack.add(root.val);
        if(root.left!=null) buildStack(root.left);
    }
    
    public int next() {
        return stack.pop();
    }
    
    public boolean hasNext() {
        return (stack.size()>0);
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
