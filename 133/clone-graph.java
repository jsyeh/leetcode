/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    //HashSet<Integer> set = new HashSet<Integer>();//了解這個Node是否有建構了
    HashMap<Integer,Node> map = new HashMap<Integer,Node>();//從val對應到ans的node
    LinkedList<Node> queue = new LinkedList<Node>();
    LinkedList<Node> queueAns = new LinkedList<Node>();
    public Node cloneGraph(Node node) {
        if(node==null) return null;
        Node ans = new Node(node.val);
        map.put(node.val, ans);
        queue.push(node);
        queueAns.push(ans);
        while(queue.size()>0){
            Node now = queue.pop();
            Node nowAns = queueAns.pop();
            for(Node next : now.neighbors){
                if(!map.containsKey(next.val)){
                    Node temp = new Node(next.val);
                    map.put(next.val, temp);
                    queue.push(next);
                    queueAns.push(temp);
                }
                Node temp = map.get(next.val);
                nowAns.neighbors.add(temp);
            }
        }
        return ans;
    }
}
