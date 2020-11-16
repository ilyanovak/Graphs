

def earliest_ancestor(ancestors, starting_node):
    graph = create_family(ancestors)
    distance = 0
    ancestor = (starting_node, distance)
    result = earliest_ancestor_helper(graph, starting_node, ancestor, distance)
    if result[1] == 0:
        return -1
    return result[0]


def create_family(ancestors):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[1])
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    return graph


def earliest_ancestor_helper(graph, currNode, ancestor, distance):
    if graph.get_neighbors(currNode) is None:
        return (currNode, distance)
    distance += 1
    for parent in graph.get_neighbors(currNode):
        result = earliest_ancestor_helper(graph, parent, ancestor, distance)
        if result[1] > ancestor[1]:
            ancestor = result
        elif result[1] == ancestor[1] and result[0] < ancestor[0]:
            ancestor = result
    return ancestor



class Graph:

    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]


    def __str__(self):
        return f'{self.vertices}'


# TEST
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)
earliest_ancestor(test_ancestors, 2)
earliest_ancestor(test_ancestors, 3)
earliest_ancestor(test_ancestors, 4)
earliest_ancestor(test_ancestors, 5)
earliest_ancestor(test_ancestors, 6)
earliest_ancestor(test_ancestors, 7)
earliest_ancestor(test_ancestors, 8)
earliest_ancestor(test_ancestors, 9)
earliest_ancestor(test_ancestors, 10)
earliest_ancestor(test_ancestors, 11)
