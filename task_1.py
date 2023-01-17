class Solution:
    def is_palindrome(self, x: 0) -> bool:
        x1 = x
        rev = 0
        if x > 0:
            while x != 0:
                last_digit = x % 10
                rev = rev * 10 + last_digit
                x = x // 10
        if rev == x1 and x1 >= 0:
            return True
        else:
            return False
