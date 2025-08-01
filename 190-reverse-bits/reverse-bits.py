class Solution:
    def reverseBits(self, n: int) -> int:
        binary=bin(n)[2:].zfill(32)
        rbinary=binary[::-1]
        return int(rbinary,2)
