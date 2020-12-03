class Solution:
    def entityParser(self, text):
        dic = {"&quot;":"\"",
               "&apos;":"\'",
               "&amp;":"&",
               "&gt;":">",
               "&lt;":"<",
               "&frasl;":"/"}
        for temp in dic:
            print(text.find(temp))
            text = text.replace(temp,dic[temp])
        return text
s = Solution()
print(s.entityParser("&amp; is an HTML entity but &ambassador; is not."))
    
