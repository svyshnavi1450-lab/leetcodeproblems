class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def generate(ind,comb,ans,candidates,target):
            if(target==0):
                ans.append(comb.copy())
                return
            if(target<0):
                return
            if(ind==len(candidates)):
                return
            comb.append(candidates[ind])
            generate(ind,comb,ans,candidates,target-candidates[ind])
            comb.pop()
            generate(ind+1,comb,ans,candidates,target)
        ind=0
        ans=[]
        comb=[]
        generate(ind,comb,ans,candidates,target)
        return ans