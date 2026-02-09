class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Trim leading whitespace
        s = s.lstrip()

        # Step 2: Handle sign
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Read digits
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Step 4: Apply the sign
        result *= sign

        # Step 5: Handle overflow
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        elif result > int_max:
            return int_max
        return result
