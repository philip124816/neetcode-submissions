class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # hash, index
        out = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            tc = tuple(count)
            if tc in res:
                index = res[tc]
                out[index].append(s)
            else:
                res[tc] = len(out)
                out.append([s])
        return out