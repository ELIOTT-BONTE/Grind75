class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def clearIsland(x, y):
            # Directions for DFS: right, left, down, up
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            # Check if (x, y) is out of bounds or is water ('0')
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                return

            # Mark the current cell as visited by changing '1' to '0'
            grid[x][y] = '0'
            
            # Explore all 4 directions
            for dx, dy in directions:
                clearIsland(x + dx, y + dy)

        # Edge case: Empty grid
        if not grid or not grid[0]:
            return 0

        num_islands = 0
        
        # Traverse the entire grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an island
                    num_islands += 1  # Increment island count
                    clearIsland(i, j)  # Call DFS to mark the whole island

        return num_islands
