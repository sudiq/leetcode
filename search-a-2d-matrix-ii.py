# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])-1
        def binary_search(arr,l=0,r=r):
            c = (l+r)//2
            if l>r:
                return False
            if arr[c] == target:
                return True
            elif arr[c]> target:
                return binary_search(arr,l,c-1)
            else:
                return binary_search(arr,c+1,r)
        for arr in matrix:
            if binary_search(arr):
                return True 
        return False