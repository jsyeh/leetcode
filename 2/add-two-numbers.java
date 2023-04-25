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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans=new ListNode();
        ListNode next = ans;
        int carry=0;
        while(l1!=null || l2!=null){
            int now = carry;
            if(l1!=null) now += l1.val;
            if(l2!=null) now += l2.val;
            carry = now/10;
            next.next = new ListNode(now%10);
            next = next.next;
            if(l1!=null) l1 = l1.next;
            if(l2!=null) l2 = l2.next;
        }
        if(carry>0) next.next = new ListNode(carry);
        return ans.next;
    }
}
