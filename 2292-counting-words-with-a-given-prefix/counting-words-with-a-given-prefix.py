class Solution:
   def prefixCount(self, words: List[str], pref: str) -> int:
       count = 0
       for i in range(len(words)):
           if pref == words[i]:
               count += 1
               continue
           if len(pref) <= len(words[i]):
               for j in range(len(pref)):
                   if pref[j] != words[i][j]:
                       break
               else:
                   count += 1
       return count
