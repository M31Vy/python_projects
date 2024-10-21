def add(A,B):
    x = 0
    i = 0
    C = []
    while x < len(A) or x<len(B):
        if x>=len(A):
            t = B[x]+i
        elif x>=len(B):
            t = A[x]+i
        else:
            t = A[x]+B[x]+i
        C.append(t%10)
        i = t//10
        x+=1
    if i>0:
        C.append(i)
    return C

def fun(A,B)->list:
    x = 0
    i = 0
    C = []
    
    while x < len(A):        
        if x>=len(B):
            t = A[x]+i
        else:
            t = A[x]-B[x]+i
        C.append(t%10)
        i = t//10
        x+=1
    return C

def ans(A,B):
    if len(A)>len(B):
        ans = fun(A,B)
        ans.append(True)
        return ans
    elif len(A)<len(B):
        ans = fun(B,A)
        ans.append(False)
        return ans
    else:
        s = len(A)
        for x in range(s):
            if A[s-x-1]>B[s-x-1]:
                ans = fun(A,B)
                ans.append(True)
                return ans
            elif A[s-x-1]<B[s-x-1]:
                ans = fun(B,A)
                ans.append(False)
                return ans
        return [0]



if __name__ == '__main__':
    A = [2,4,4]
    B = [2,6,4]
    print(ans(A,B))
    # A = [9,9,9,9,9,9,9]
    # B = [9,9,9,9]
    # print(add(A,B))
    # A = [0]
    # B = [0]
    # print(add(A,B))
    # A = [9,9,9,9,9,9,9]
    # B = [9,9,9,9]
    # print(add(A,B))
    # A = [1,2,3,4,5,6,7,8,9]
    # B = [9,8,7,6,5,4,3,2,1]
    # print(add(A,B))