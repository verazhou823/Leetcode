class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        def swap(a,b):
            if a == b:
                return
            for i in range((b-a)/2+1):
                s[a+i],s[b-i] = s[b-i],s[a+i]
        if len(s)<=1:
            return
        swap(0,len(s)-1)
        start = 0
        i = 0
        while(i <len(s)):
            if s[i] == " ":
                swap(start,i-1)
                start = i+1
            i += 1
        swap(start,len(s)-1)
s = Solution()
string = ["a"," ","a"]
s.reverseWords(string)
print(string)

