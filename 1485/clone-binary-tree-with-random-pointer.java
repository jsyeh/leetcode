/**
 * Definition for Node.
 * public class Node {
 *     int val;
 *     Node left;
 *     Node right;
 *     Node random;
 *     Node() {}
 *     Node(int val) { this.val = val; }
 *     Node(int val, Node left, Node right, Node random) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *         this.random = random;
 *     }
 * }
 */

class Solution {
    //後來看了 Solution 裡，有人用 dfs() 配合 map 做出來
    public NodeCopy dfs(Node root, Map<Node,NodeCopy> map) {
        if(root==null) return null;
        if(map.containsKey(root)) return map.get(root);
        //這裡的 HasmMap 還不熟

        NodeCopy ans = new NodeCopy(root.val);
        map.put(root, ans);
        //這裡的 HasmMap 還不熟

        ans.left = dfs(root.left, map);
        ans.right = dfs(root.right, map);
        ans.random = dfs(root.random, map);

        return ans;
    }
    public NodeCopy copyRandomBinaryTree(Node root) {
        Map<Node,NodeCopy> map = new HashMap<Node,NodeCopy>();
        return dfs(root, map);
    }
}
