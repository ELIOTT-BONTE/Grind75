class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:


        rows, cols = len(mat), len(mat[0])
        queue = deque()
        # populate distance matrix with infinities
        dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]

        # for each 0 in original matrix, create a corresponding 0 in distance matrix
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))


        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # for each square with a value, update its neighbouts to be of the same value +1, or its own current value, whatever the minimum is

        while queue :
            x, y = queue.popleft()
            for dx, dy in directions:
                if 0 <= x + dx < rows and 0 <= y + dy < cols :
                    if dist[x + dx][y + dy] > dist[x][y] + 1 :
                        dist[x + dx][y + dy] = dist[x][y]+1
                        queue.append((x + dx, y + dy))

        return dist