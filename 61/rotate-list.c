/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k){
    //要先知道 nodes數量N, 以便 k%N
    int N = 0;
    struct ListNode* next = head;
    struct ListNode* end = NULL;
    while(next!=0){
        N++;
        end = next;//順便記錄最後一格的位置
        next = next->next;
    }
    
    if(N==0) return head;
    k = N - k%N - 1; //表示往右k格

    //突然有個idea: 把頭尾相接,變成環狀, 之後再拆開, 好像就好了
    end->next = head;

    next = head;
    for(int i=0; i<k; i++){
        next = next->next;
    }
    struct ListNode * ans = next->next; //如果 k 剛好是 N-1 的話,就會走到最後而錯
    next->next = NULL;
    //end->next = head;

    return ans;
}
//case 2/231: [] 0
//case 41/231: [1,2] 1
//我的測試:[1,2,3,4,5,6,7,8,9,10] 7
// [1,2,3,4,5,6,7,8,9,10] 9
