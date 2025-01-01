# bruteforce

import math
import numpy as np

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        r = []
        for point in points:
            dist = math.sqrt((point[0]**2)+(point[1]**2))
            res.append([point[0],point[1], dist])
            res.sort(key = lambda x: x[2])
            # print(res)
        for i in range(k):
            r.append([res[i][0], res[i][1]])
        return r