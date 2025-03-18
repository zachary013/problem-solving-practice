

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {

    public boolean hasCycle(ListNode head) {
        ListNode p = head;
        ListNode q = head;

        while (p != null && p.next != null) {
            q = q.next;
            p = p.next.next;

            if (p == q) {
                return true;
            }
        }

        return false;
    }
}
