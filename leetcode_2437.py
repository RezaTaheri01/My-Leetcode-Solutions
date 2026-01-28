class Solution:
    def countTime(self, time: str) -> int:
        hh, mm = time.split(":") 
        times = 1

        # Minutes
        if mm[0] == "?":
            times *= 6
        if mm[1] == "?":
            times *= 10

        # Hours
        if hh == "??":
            times *= 24
            
        elif hh[0] == "?":
            if int(hh[1]) < 4:
                times *= 3
            else:
                times *= 2
        elif hh[1] == "?":
            if hh[0] == "2":
                times *= 4
            else:
                times *= 10

        return times
    
    
    
s = Solution()

print(s.countTime("??:??"))
print(s.countTime("?2:??"))
print(s.countTime("?2:?5"))
print(s.countTime("2?:??"))
print(s.countTime("?4:22"))
