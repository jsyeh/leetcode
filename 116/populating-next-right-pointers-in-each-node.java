/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    ArrayList<Node> prev = new ArrayList<Node>();
    public Node connect(Node root) {
        if(root==null) return null;
        connect(root, 0);
        for(Node last : prev){
            last.next = null;
        }
        return root;
    }
    void connect(Node root, int level){
        if(root==null) return;
        if(prev.size()<=level){
            prev.add(root);
        }else{
            Node p = prev.get(level);
            p.next = root;
            prev.set(level, root);
        }
        connect(root.left, level+1);
        connect(root.right, level+1);
    }
}
