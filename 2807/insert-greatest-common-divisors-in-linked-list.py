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
    int gcd(int a, int b){
        if(a==0) return b;
        if(b==0) return a;
        return gcd(b, a%b);
    }
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode ans = head;
        ListNode next = head.next;
        while(next!=null){
            int a = head.val, b = next.val;
            ListNode mid = new ListNode(gcd(a, b), next);
            head.next = mid;
            head = next;
            next = next.next;
        }
        return ans;
        
    }
}
