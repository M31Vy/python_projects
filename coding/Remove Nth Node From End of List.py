def rem(head,n):
    N=ListNode(0)
    N.next=head
    i=N
    j=N
    for x in range(n):
        j=j.next
    while j.next:
        i=i.next
        j=j.next
    i.next=i.next.next
    return N.next

def main(head,n):
    i=head
    j=head
    for x in range(n+1):
        if not j:
            return head.next
        j=j.next
    while j:
        i=i.next
        j=j.next
    i.next=i.next.next
    return head