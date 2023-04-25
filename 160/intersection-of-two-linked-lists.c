/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    //研究答案的寫法，發現 two pointers的方法很帥又很簡單，試寫看看
    struct ListNode *p1 = headA;
    struct ListNode *p2 = headB;

    while(true){
        if(p1==p2) return p1;
        if(p1==NULL) p1=headB;
        else p1 = p1->next;
        if(p2==NULL) p2=headA;
        else p2 = p2->next;
    }

}
