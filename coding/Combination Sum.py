def combinationSum(candidates, target):
    n=len(candidates)
    ans = []
    def fun(i,sum,temp,n,target,ans,candidates):
        if sum>target:
            return
        if sum==target:
            ans.append(temp)
            return
        for j in range(i,n):
            if sum+candidates[j]<=target:
                fun(j,sum+candidates[j],temp+[candidates[j]],n,target,ans,candidates)
            else:
                continue

    fun(0,0,[],n,target,ans,candidates)
    return ans

def combinationSum_2(candidates, target):
    candidates.sort()
    n=len(candidates)
    ans = []
    def fun(i,sum,temp,n,target,ans,candidates):
        if sum>target:
            return
        if sum==target:
            ans.append(temp)
            return
        for j in range(i,n):
            if sum+candidates[j]<=target:
                fun(j,sum+candidates[j],temp+[candidates[j]],n,target,ans,candidates)
            else:
                break

    fun(0,0,[],n,target,ans,candidates)
    return ans

if __name__ == '__main__':
    print(combinationSum([8,7,4,3],11))
    print(combinationSum([2,3,6,7],7))