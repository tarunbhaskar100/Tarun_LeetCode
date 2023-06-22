class Solution:
    def reverse(self, x: int) -> int:
        si = str(x)[::-1]
        if si[-1] == '-':
            if ((-2)**31) <=int(si[:-1])*(-1) <= ((2**31) - 1):
                return int(si[:-1])*(-1)
            else:
                return 0
        else:
            if ((-2)**31) <= int(si) <= ((2**31) - 1):
                return int(si)
            else:
                return 0