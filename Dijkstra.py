import sys
class Dijkstra(object):
    def __init__(self,array):
        self.array = array
        self.distance = [sys.maxint for i in range(len(array))]
        self.visited = set()
        self.unvisited = set()
        for i in range(len(array)):
            self.unvisited.add(i)

    def shortPath(self,source):
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i][j] ==0:
                    array[i][j] = sys.maxint
        self.distance[source] = 0
        nextNode = source
        while(self.unvisited):
            self.visited.add(nextNode)
            self.unvisited.remove(nextNode)
            for i in range(len(self.array)):
                self.distance[i] = min(self.distance[i],self.distance[nextNode] + array[nextNode][i])
            minimum = sys.maxint
            for i in self.unvisited:
                if self.distance[i] <minimum:
                    minimum = self.distance[i]
                    nextNode = i
        return self.distance


array = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
dijk = Dijkstra(array)
print(dijk.shortPath(0))
