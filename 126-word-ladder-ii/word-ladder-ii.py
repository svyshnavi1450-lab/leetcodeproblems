class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return[]
        par={}
        found=False
        lev=set([beginWord])
        while lev and not found:
            nl=set()
            for word in lev:
                if word in wordset:
                    wordset.remove(word)
            for word in lev:
                for i in range(len(word)):
                    for ch in 'qwertyuioplkjhgfdsazxcvbnm':
                        nw=word[:i]+ch+word[i+1:]
                        if nw in wordset:
                            if  nw not in par:
                                par[nw]=[]
                            par[nw].append(word)
                            nl.add(nw)
                            if nw==endWord:
                                found=True
            lev=nl
        res=[]
        def dfs(word,path):
            if word==beginWord:
                res.append(path[::-1])
                return
            if word not in par:
                return
            for p in par[word]:
                dfs(p,path+[p])
        if found:
            dfs(endWord,[endWord])
        return res
        
        