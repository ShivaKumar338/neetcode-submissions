from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         new ={}
#         result =[]
#         for i in range(len(strs)):
#             for j in range(i+1,len(strs)):
#                 if Counter(strs[i])==Counter(strs[j]):
#                     result[i].append(strs[j])
#         return result