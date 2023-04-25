/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 //寫不出來，先改用Java試試
struct ListNode* deleteDuplicates(struct ListNode* head){
    if(head==NULL) return head;
    if(head->next==NULL) return head;

    struct ListNode ans;
    ans.next = head;
    struct ListNode * p1 = &ans;
    struct ListNode * p2 = p1->next;
    int dupN=1;
    while(p2!=NULL){
        if(p2->next!=NULL){
            if(p2->val == p2->next->val){
                dupN++;
                printf("==, %d %d\n", p1->val, p2->val);
                printf("dupN:%d\n", dupN);
            } else{ 
                if(dupN==1){
                    p1->next = p2;
                    p1 = p1->next;
                }
                dupN=1;
            }
        }else{//p2->next==NULL
            if(dupN==1){
                p1->next = p2;
                p2->next = NULL;
            }
        }
        p2 = p2->next;
    }
    if(dupN==1) p1->next->next = NULL;
    else p1->next=NULL;
    
    return ans.next;
}//case 86/166: [1,1]
