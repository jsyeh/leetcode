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
    List<List<Integer>> lists = new ArrayList<List<Integer>>();
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        zigzagLevelOrder(root, 0);
        for(int level=0; level<lists.size(); level++) {
            if(level%2==0) { //left to right
                //不用動
            } else { //right to left
                List<Integer> list = lists.get(level);
                int N = list.size();
                for(int i=0; i<N/2; i++) {
                    int a = list.get(i), b = list.get(N-1-i);
                    list.set(i, b);
                    list.set(N-1-i, a);
                }
            }
        }
        return lists;
    }
    void zigzagLevelOrder(TreeNode root, int level) {
        if(root==null) return;
        if(lists.size()<=level){
            List<Integer> list = new ArrayList<Integer>();
            lists.add(list);
        }
        lists.get(level).add(root.val);
        zigzagLevelOrder(root.left, level+1);
        zigzagLevelOrder(root.right, level+1);
    }
}
