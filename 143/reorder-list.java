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
    void showList(ListNode head) { //印出來, 供debug理解
        while(head!=null){
            System.out.print(" - " + head.val);
            head = head.next;
        }
        System.out.println();
    }

    public void reorderList(ListNode head) {
//showList(head);
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next!=null && fast.next.next!=null){ //會早一點點撞邊結束
            fast = fast.next.next;
            slow = slow.next;
        } //可找到中間的點
        ListNode mid = slow.next;//新的開始
        slow.next = null;//斷開

//showList(mid);
        ListNode next = mid;
        ListNode rev = new ListNode(); //獨立在外的點,rev.next後面才是主角
        while(next!=null){ //逆轉接法
            ListNode temp = next.next; //下一筆,等一下要接好

            next.next = rev.next; //next右接好
            rev.next = next; //next左接好
            
            next = temp; //到下一筆
        }
        rev = rev.next;
//showList(head);
//showList(rev);
        while(rev!=null){
            ListNode temp1 = head.next; //下一筆,等一下要接好
            ListNode temp2 = rev.next; //下一筆,等一下要接好
            head.next = rev; //插進來 (交錯,插入)
            rev.next = temp1; //接好
            head = temp1; //新的開始
            rev = temp2; //新的開始
        }
    }
}
