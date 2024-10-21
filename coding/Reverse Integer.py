def fun(x):
    if x<0:
        i=-1
        x=-x
    else:
        i=1

    ans = 0
    while x!=0:
        y=x%10
        ans=ans*10+y
        x=x//10

    if ans < -2**31 or ans > 2**31 - 1:
        return 0
    return ans*i

def fun_2(x):
    if x<0:
        ans = -int(str(-x)[::-1])
    else:
        ans = int(str(x)[::-1])

    if ans < -2**31 or ans > 2**31 - 1:
        return 0
    return ans

if __name__ == '__main__':
    x=123
    print(fun(x))