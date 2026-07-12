class Solution(object):
    def longestCommonPrefix(self, strs):
        ans=strs[0]
        for elements in strs:
            for i in range(min(len(elements),len(ans))):
                if ans[i]!=elements[i]:
                    ans=ans[:i]
                    break
            else:
                ans=ans[:min(len(elements),len(ans))]
        return ans