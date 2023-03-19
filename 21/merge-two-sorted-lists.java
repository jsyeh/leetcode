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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head= new ListNode();
        ListNode node=head;
        while(list1!=null && list2!=null){
            if(list1.val<list2.val){
                node.next = new ListNode(list1.val);
                list1 = list1.next;
                node = node.next;
            } else {
                node.next = new ListNode(list2.val);
                list2 = list2.next;
                node = node.next;
            }
        }
        if(list1==null) {
            node.next = list2;
        } else if(list2==null){
            node.next = list1;
        }
        return head.next;
    }
}
