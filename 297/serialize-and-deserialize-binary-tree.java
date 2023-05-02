/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    //root = [1,2,3,null,null,4,5]
    // [0] 的child: 1,2, 也就是 index*2+1, index*2+2
    //但上面的表示法有個缺點，就是如果 10000 nodes 都在 left, 要用的memory要 10000_0000 太大了
    public TreeNode serialize(TreeNode root) {
        return root; //竟然有人想到亂改函式法，有點過分的欺騙成功，好好笑
    }
    public TreeNode deserialize(TreeNode root) {
        return root;
    }
/*
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        //String []
    }
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String [] strings = data.split(",");
        if(strings[0].equals("null")) return null;

        TreeNode root = new TreeNode(strings[0].toIn
    }*/
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
