def mergeKLists(lists):
    def mergeTwoLists(l1, l2):
        if not l2:
            return l1
        if not l1:
            return l2
        if l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2
    
    if not lists:
        return None
    while len(lists) > 1:
        N = []
        for i in range(0, len(lists), 2):
            if i+1 < len(lists):
                N.append(mergeTwoLists(lists[i], lists[i+1]))
            else:
                N.append(lists[i])
        lists = N
    return lists[0]

def msort(lists):
    if len(lists) == 1:
        return lists[0]
    N = []
    for i in range(0, len(lists), 2):
        if i+1 < len(lists):
            N.append(mergeTwoLists(lists[i], lists[i+1]))
        else:
            N.append(lists[i])
    return msort(N)