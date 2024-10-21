def sub(S):
    A=set()
    i=0
    ans=''
    for j in range(len(S)):
        if S[j] not in A:
            A.add(S[j])
            if j == len(S)-1:
                if len(A)>len(ans):
                    ans=S[i:]
        else:
            if len(A)>len(ans):
                ans=S[i:j]
            while S[i]!=S[j]:
                A.remove(S[i])
                i+=1
            i+=1
    return ans

if __name__ == "__main__":
    L = ["abcdabcdefbb", "bbbbb", "pwwkew",'','a','ab','abc','abca','abcabcbb']
    for S in L:
        print(sub(S))
