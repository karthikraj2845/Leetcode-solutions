class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        num_rows = len(grid)
        num_cols = len(grid[0])
        result = [[0] * num_cols for _ in range(num_rows)]
        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                flat_position = row_idx * num_cols + col_idx
                new_flat_position = (flat_position + k) % (num_rows * num_cols)
                new_row, new_col = divmod(new_flat_position, num_cols)
                result[new_row][new_col] = value
      
        return result

        