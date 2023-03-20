/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 public class Solution {
     //使用 fast-slow 法
     public ListNode detectCycle(ListNode head) {
         ListNode fast = head;
         ListNode slow = head;
         if(head==null) return null;
         while(fast.next!=null && fast.next.next!=null) {
             //走到終點，有結尾，就不是Cycle
             fast = fast.next.next; //兩倍數
             slow = slow.next; //慢慢走
             if(fast==slow) break;
         }
         if(fast.next==null || fast.next.next==null) return null;

         while(slow!=head) {
             slow = slow.next;
             head = head.next;
         }
         return head;
     }
 }
