class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only 1 row, return the string as is
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array for each row
        rows = [''] * numRows
        curr_row = 0
        step = 1  # direction: down (1) or up (-1)

        for ch in s:
            rows[curr_row] += ch
            # Change direction when reaching top/bottom
            if curr_row == 0:
                step = 1
            elif curr_row == numRows - 1:
                step = -1
            curr_row += step

        return ''.join(rows)
