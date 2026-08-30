class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer limits
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # 1. Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # 2. Determine sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # 3. Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # 4. Perform bitwise division
        while a >= b:
            temp = b
            multiple = 1
            # Double 'temp' using bit shift until it exceeds 'a'
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            a -= temp
            quotient += multiple

        # 5. Apply sign and clamp result
        res = -quotient if negative else quotient
        return max(MIN_INT, min(MAX_INT, res))