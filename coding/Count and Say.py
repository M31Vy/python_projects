def countAndSay(n: int):
    if n==1:
        return "1"
    before = '1'
    after = ''
    while n>1:
        temp = before[0]
        count = 0
        for x in before:
            if x==temp:
                count += 1
            else:
                after += str(count) + temp
                temp = x
                count = 1
        before = after + str(count) + temp
        after = ''
        n -= 1
    return before