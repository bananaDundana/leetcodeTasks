class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        for c in s:
            if 'IV' in s:
                count += 4
                s = s.replace('IV', '')
            if 'IX' in s:
                count += 9
                s = s.replace('IX', '')
            if 'XL' in s:
                count += 40
                s = s.replace('XL', '')
            if 'XC' in s:
                count += 90
                s = s.replace('XC', '')
            if 'CD' in s:
                count += 400
                s = s.replace('CD', '')
            if 'CM' in s:
                count += 900
                s = s.replace('CM', '')
        count += s.count('I') + s.count('V') * 5 + s.count('X') * 10 + s.count('L') * 50 + s.count('C') * 100 + s.count('D') * 500 + s.count('M') * 1000
        return count