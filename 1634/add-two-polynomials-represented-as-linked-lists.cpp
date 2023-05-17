/**
 * Definition for polynomial singly-linked list.
 * struct PolyNode {
 *     int coefficient, power;
 *     PolyNode *next;
 *     PolyNode(): coefficient(0), power(0), next(nullptr) {};
 *     PolyNode(int x, int y): coefficient(x), power(y), next(nullptr) {};
 *     PolyNode(int x, int y, PolyNode* next): coefficient(x), power(y), next(next) {};
 * };
 */

class Solution {
public:
    PolyNode* addPoly(PolyNode* poly1, PolyNode* poly2) {
        PolyNode * ans = new PolyNode();
        PolyNode * next = ans;
        while(poly1!=nullptr && poly2!=nullptr) {
            if(poly1->power > poly2->power){
                next->next = poly1;
                poly1 = poly1->next;
                next = next->next;
            } else if(poly2->power > poly1->power) {
                next->next = poly2;
                poly2 = poly2->next;
                next = next->next;
            } else { //equal power
                int coeff = poly1->coefficient+poly2->coefficient;
                if(coeff!=0){
                    next->next = new PolyNode(coeff, poly1->power);
                    next = next->next;
                }
                poly1 = poly1->next;
                poly2 = poly2->next;
            }
        }
        if(poly1==nullptr) next->next = poly2;
        else if(poly2==nullptr) next->next = poly1;

        return ans->next;
    }
};
