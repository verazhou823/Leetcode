class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bankset = set(bank)
        if not bankset:
            return -1
        if start in bankset:
            bankset.remove(start)
        if end not in bankset:
            bankset.add(end)
        front = set()
        front.add(start)
        tail = set()
        tail.add(end)
        length = 0
        while front:
            newset = set()
            for i in front:
                for j in xrange(8):
                    for k in "ACGT":
                        if i[0:j]+k+i[j+1:] in bankset and i[0:j]+k+i[j+1:]!=i:
                            newset.add(i[0:j]+k+i[j+1:])
            length +=1
            bankset -= front
            front = newset
            if front & tail:
                return length
            print(front)
            print(bankset)
            if len(front)>len(tail):
                front,tail = tail,front

        return -1


solution = Solution()
start = "AAAAAAAA"
end = "CCCCCCCC"
bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
print(solution.minMutation(start,end,bank))


