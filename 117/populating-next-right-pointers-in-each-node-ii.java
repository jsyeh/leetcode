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
    ArrayList<ArrayList<Node>> trace = new ArrayList<ArrayList<Node>>();

    public Node connect(Node root) {
        travelAndTrace(root, 0);
        for(ArrayList<Node> row : trace) {
//System.out.println("level"+row.size());
            for(int i=0; i<row.size(); i++) {
                Node now = row.get(i);
                if(i==row.size()-1) {
                    now.next = null;
//System.out.print('#');
                } else {
                    now.next = row.get(i+1);
//System.out.print(i+1);
                }
            }
//System.out.println();
        }
        return root;
    }

    void travelAndTrace(Node root, int level) {
        if(root==null) return;
        if(trace.size()<=level){
            ArrayList<Node> temp = new ArrayList<Node>();
            temp.add(root);
            trace.add(temp);
        }else{
            trace.get(level).add(root);
        }
        travelAndTrace(root.left, level+1);
        travelAndTrace(root.right, level+1);
    }

}
