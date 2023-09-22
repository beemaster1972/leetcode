class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows >= length:
            return s
        num_columns = (numRows - 2) * (length - numRows * (length // numRows)) + length//numRows
        conversion_matrix = [[""] * num_columns] * numRows
        print(conversion_matrix)
        index = 0
        for column in range(num_columns):
            if not num_columns % (column + 1):
                for row in range(numRows):
                    conversion_matrix[row][column] = s[index]
                    index += 1
        print(conversion_matrix)
        return "".join([c for row in conversion_matrix for c in row])


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("abcdefghijklmnopqrstuvwxyz", 5))
