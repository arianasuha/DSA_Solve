class Solution:
    def romanToInt(self, s: str) -> int:
       
        new_dict = {
            "I": 1, "V": 5 , "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }
        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and new_dict[s[i]] < new_dict[s[i + 1]]:
                result += new_dict[s[i + 1]] - new_dict[s[i]]
                i += 2
            else:
                result += new_dict[s[i]]
                i += 1
        return result



# Testcase
roman = "III"
s1 = Solution()
print(s1.romanToInt(roman))
roman = "LVIII"
print(s1.romanToInt(roman))
roman = "MCMXCIV"
print(s1.romanToInt(roman))