class Solution(object):
    def rotateRight(self, head, k):
        r1 = []
        current = head

        while current:
            r1.append(current.val)
            current = current.next

        l = len(r1)
        if l == 0:
            return None

        k = k % l
        if k == 0:
            return head

        for _ in range(k):
            r = r1.pop()
            r1.insert(0, r)

        head1 = ListNode(r1[0])
        current1 = head1
        for i in range(1, l):
            current1.next = ListNode(r1[i])
            current1 = current1.next

        return head1