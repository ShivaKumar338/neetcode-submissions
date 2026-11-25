from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        # answer = defaultdict(list)

        # for s in strs:
        #     count =[0]*26
        #     for c in s:
        #         count[ord(c)-ord('a')]+=1
        #     answer[tuple(count)].append(s)
        #     # answer["".join(sorted(s))].append(s)
        
        # return list(answer.values())
        
        ans = defaultdict(list)
        for i in  strs:
            ans["".join(sorted(i))].append(i)
        return list(ans.values())