def pal(s):
    if len(s)==0 or len(s)==1:
        return s
    ans=''
    for x in range(len(s)-1):
        i=x-1
        j=x+1
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        if j-i-1>len(ans):
            ans=s[i+1:j]
        
        i=x
        j=x+1
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        if j-i-1>len(ans):
            ans=s[i+1:j]
    return ans

if __name__ == "__main__":
    L = ["babad", "cbbd", "a", "ac", "bb", "ab", "abc", "abca", "abcabcbb"]
    for s in L:
        print(pal(s))