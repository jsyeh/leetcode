/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null) return head;
        ListNode temp = head.next;
        ListNode prev = head;
        while(temp!=null) {
            if(temp.val == prev.val){
                temp = temp.next;
                if(temp==null){
                    prev.next = null;
                }
            }else{
                prev.next = temp;
                temp = temp.next;
                prev = prev.next;
            }
        }
        return head;
    }
}
