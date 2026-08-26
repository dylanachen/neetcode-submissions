class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        time = 0

        # we make the queue of the rotten oranges with their coord pairs
        # we also count all the fresh oranges
        # as we iterate time, if fresh oranges doesn't change, but is still >0, then we cannot rot all oranges
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while fresh > 0 and queue:
            for i in range(len(queue)):
                curr_row, curr_col = queue.popleft()

                for row_diff, col_diff in directions:
                    row, col = curr_row + row_diff, curr_col + col_diff

                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1