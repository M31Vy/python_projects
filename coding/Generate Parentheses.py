def generateParenthesis(n):
    def helper(l,r,s,ans):
        if not r:
            ans.append(s)
            return
        if l:
            helper(l-1,r,s+'(',ans)
        if r>l:
            helper(l,r-1,s+')',ans)

    ans=[]
    helper(n,n,'',ans)
    return ans