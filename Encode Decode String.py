class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        answer  = ""
        for i in range(len(strs)):
            answer += str(len(strs[i]))
            answer += ":"
            answer += strs[i]
        return answer

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        answer = []
        i = 0
        while(i<len(s)):
            temp = int(s[i])
            while(s[i+1] != ":"):
                i += 1
                temp = temp*10+int(s[i])
            i += 2
            j = i+temp
            answer.append(s[i:j])
            i = j
        return answer
# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = ["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "]
print(codec.encode((strs)))
print(codec.decode(codec.encode(strs)))
