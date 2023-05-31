/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
//需要 HashMap 幫忙對應 old to new
//然後走2輪, 第1輪建map, 第2輸照著map建random連結
class Solution {
    HashMap<Node,Node> map = new HashMap<>();
    public Node copyRandomList(Node head) {
        if(head==null) return null;
        //case: 3/19: [] 空指標
        Node ans = new Node(head.val);
        map.put(head, ans);

        Node next = head.next;
        Node next2 = ans;
        while(next != null) {
            Node temp = new Node(next.val);
            map.put(next, temp);
            next2.next = temp;
            next2 = next2.next;
            next = next.next;
        }//第一輪,照著值建出結構

        next = head;
        next2 = ans; //第二輪, 查 map 確認 random值
        while(next != null){
            next2.random = map.get(next.random);
            next2 = next2.next;
            next = next.next;
        }
        return ans;
    }
}
