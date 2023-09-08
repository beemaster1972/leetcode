class Solution(object):
    def generate(self, numRows: int) -> list[list[int]]:
        """
        type numRows: int
        rtype: List[List[Int]]
        """
        
        def get_element_by_coords(lst: list[list[int]], i:int,j:int)->int:
            if j == 0 or j== i:
                return 1
            return lst[i-1][j-1]+lst[i-1][j]
        

        result = [[1]]
        for i in range(1,numRows):
            row = [get_element_by_coords(result,i,j) for j in range(i+1)]
            result.append(row)
        return result
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(30))
