def longestValidParentheses(s):
    max_length = 0
    temp = [-1]
 
    for i in range(len(s)):
        if s[i] == '(':
            temp.append(i)
        else:
            temp.pop()
            if not temp:
                temp.append(i)
            else:
                max_length = max(max_length, i - temp[-1])
    
    return max_length