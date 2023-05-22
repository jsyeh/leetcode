/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        if(head==null) return head;
        head.next = flatten(head.next);
        if(head.child != null){
            Node child = flatten(head.child);
            head.child = null;

            Node temp = child;
            while(temp.next!=null){
                temp = temp.next;
            }
            temp.next = head.next;
            if(head.next!=null) head.next.prev = temp;

            head.next = child;
            child.prev = head;
        }

        return head;
    }
}//cast 7/26: [1,null,2,null,3,null]
