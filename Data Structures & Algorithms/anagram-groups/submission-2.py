class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sols = []
        list_hash = []
        for x in strs:
            l_hash = {}
            for y in x:
                if y in l_hash:
                    l_hash[y] +=1
                else:
                    l_hash[y] = 1
            list_hash.append(l_hash)
        
        for x in range(len(strs)):
            s = []
            for y in range(len(strs)):
                if list_hash[x] == list_hash[y]:
                    s.append(strs[y])
            if s not in sols:
              sols.append(s)
        
        return sols