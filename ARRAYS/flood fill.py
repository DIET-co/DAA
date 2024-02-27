class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        orgColor = image[sr][sc]
        
        def helper(row, col):
            if not(0 <= row < n and 0 <= col < m) or image[row][col] != orgColor:
                return
            
            image[row][col] = newColor

            helper(row - 1, col)
            helper(row + 1, col)
            helper(row, col - 1)
            helper(row, col + 1)
        
        if orgColor != newColor:
            helper(sr, sc)
        
        return image