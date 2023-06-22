class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        out =[]
        # words2 = words.copy()
        for i in range(len(s)-len("".join(words))+1):
            d = s[i:i+len("".join(words))]
            words2 = words.copy()
            for j in range(0,len("".join(words)),len(words[0])):
                if d[j:j+len(words[0])] not in words2:
                    break
                else:
                    words2.remove(d[j:j+len(words[0])])
            if words2 == []:
                out.append(i)
        return out
                    