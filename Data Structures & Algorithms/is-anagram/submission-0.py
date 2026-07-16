class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def check_letter(s):
            hm={}
            for i in range(len(s)):
                if s[i] not in hm:
                    hm[s[i]]=1
                else:
                    hm[s[i]]+=1
            return hm
        if check_letter(s) ==  check_letter(t):
            return True
        else:
            return False
        