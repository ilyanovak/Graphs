"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            print(f'Error! {v1} is already a vertex in the graph')

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print(f'Error! {v1} is not a vertex in the graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print(f'Error! {vertex_id} is not a vertex in the graph')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        discovered = set()
        queue = deque()
        queue.appendleft(starting_vertex)
        while len(queue) > 0:
            v = queue.pop()
            if v not in discovered:
                discovered.add(v)
                print(v)
                for edge in self.get_neighbors(v):
                    queue.appendleft(edge)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        discovered = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            v = stack.pop()
            if v not in discovered:
                discovered.add(v)
                print(v)
                for edge in self.get_neighbors(v):
                    stack.append(edge)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        self.dft_recursive_util(starting_vertex, visited)

    def dft_recursive_util(self, currVertex, visited):
        visited.add(currVertex)
        print(currVertex)
        for neighbor in self.get_neighbors(currVertex):
            if neighbor not in visited:
                self.dft_recursive_util(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        discovered = set()
        currPath = []
        queue = deque()
        queue.appendleft(starting_vertex)
        while len(queue) > 0:
            v = queue.pop()
            currPath.append(v)
            if v == destination_vertex:
                return currPath
            if v not in discovered:
                discovered.add(v)
                print(v)
                for edge in self.get_neighbors(v):
                    queue.appendleft(edge)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        discovered = set()
        stack = deque()
        stack.append([starting_vertex])
        while len(stack) > 0:
            currPath = stack.pop()
            currVertex = currPath[-1]
            if currVertex == destination_vertex:
                return currPath
            if currVertex not in discovered:
                discovered.add(currVertex)
                for neighbor in self.get_neighbors(currVertex):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        path = []
        return self.dfs_recursive_util([starting_vertex], destination_vertex, visited)

    def dfs_recursive_util(self, currPath, destination_vertex, visited):
        currVertex = currPath[-1]
        if currVertex == destination_vertex:
            return currPath
        visited.add(currVertex)
        for neighbor in self.get_neighbors(currVertex):
            if neighbor not in visited:
                newPath = list(currPath)
                newPath.append(neighbor)
                result = self.dfs_recursive_util(newPath, destination_vertex, visited)
                if result is not None:
                    return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    graph.dft(1)
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
