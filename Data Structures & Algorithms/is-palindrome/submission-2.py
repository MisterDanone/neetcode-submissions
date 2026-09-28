class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '').replace('?','').replace('!','').replace('.','').replace(',','').replace("'", '').replace(':','')
        
        if s == s[::-1]:
            return True
        return False
        
        
