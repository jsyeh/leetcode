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
    int ans=1;
    HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();//map對應 level vs. first index
    public int widthOfBinaryTree(TreeNode root) {
        dfs(root, 0, 0);
        return ans;
    }
    void dfs(TreeNode root, int level, int dist) {
        //dist表示離完美binary tree 最左邊的距離
        if(root==null) return;
        if(!map.containsKey(level)){
            map.put(level, dist);
        }else{
            if(dist-map.get(level)+1>ans) ans = dist-map.get(level)+1;
        }
        dfs(root.left, level+1, dist*2);
        dfs(root.right, level+1, dist*2+1);
    }
}//case4: [1]
