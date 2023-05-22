/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    
    public Node() {
        children = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        children = new ArrayList<Node>();
    }
    
    public Node(int _val,ArrayList<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    int maxD = 0;
    public int diameter(Node root) {
        height(root);
        return maxD;
    }
    int height(Node root) {
        if(root==null) return -1;
        int max = 0, max2 = 0;
        for(Node child : root.children) {
            int now = height(child) + 1;
            if(now>max){
                max2 = max;
                max = now;
            }else if(now>max2){
                max2 = now;
            }
        }
        if(max + max2 > maxD) maxD = max + max2;
        return max;
    }
}
