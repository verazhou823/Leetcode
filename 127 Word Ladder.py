from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        n = len(beginWord)
        q = deque()
        p = deque()
        q.append(beginWord)
        p.append(endWord)
        dic = {}
        dicEnd = {}
        level = 1
        levelEnd = 1
        if beginWord in wordlist:
            wordlist.remove(beginWord)
        flag = 0
        while(q and p and flag ==0):
            if len(q) > len(p):
                p,q = q,p
                dic,dicEnd = dicEnd,dic
                level,levelEnd = levelEnd,level
            count = len(q)
            number = 0
            removed = set()
            for j in range(count):
                node = q.popleft()
                for i in xrange(n):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if node[:i]+ch+node[i+1:] in wordlist:
                            dic[str(level)+str(number)] = [str(level-1)+str(j),node]
                            q.append(node[:i]+ch+node[i+1:])
                            if node[:i]+ch+node[i+1:] not in removed:
                                removed.add(node[:i]+ch+node[i+1:])
                            if node[:i]+ch+node[i+1:] in p:
                                flag = 1
                            number += 1
            if removed:
                for element in removed:
                    wordlist.remove(element)
            level += 1
        print dic
        print dicEnd

solution = Solution()
beginWord = "hit"
endWord = "cog"
wordlist = {"hot","dot","dog","lot","log"}
print(solution.ladderLength(beginWord,endWord,wordlist))
