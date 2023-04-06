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
    public ListNode removeElements(ListNode head, int val) {
        ListNode temp = head;
        ListNode ans = new ListNode();
        ListNode temp2 = ans;
        while(temp!=null){
            if(temp.val!=val){
                temp2.next = temp;
                temp = temp.next;
                temp2 = temp2.next;               
            }else{
                temp = temp.next;
                temp2.next = null;
            }
        }
        return ans.next;
    }
}
