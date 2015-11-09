import heapq

__author__ = 'rain'
from collections import defaultdict

"""
This class was copied from gist https://gist.github.com/econchick/4666413
"""


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node][to_node] = distance

    def dijkstra(self, source):
        priority_queue = []
        # The cost is 0, because the distance between source to itself is 0
        heapq.heappush(priority_queue, (0, source))
        visited = {}
        # basically the same as a normal BFS
        while priority_queue:
            # dequeue from the priority queue
            # dequeue the minimum cost path
            (current_distance, current) = heapq.heappop(priority_queue)

            # When we extract min from the priority queue
            # we know that we have found the minimum cost path to this node
            # so we consider it visited
            visited[current] = current_distance

            if current not in self.edges: continue
            for neighbour, distance in self.edges[current].items():
                # We only continue to explore neighbours that have been visited
                # (same as a normal BFS)
                if neighbour in visited: continue
                # If we haven't found the min cost path to this node, we push the new distance back onto the queue
                # because this is a min queue, if the new distance is the new min cost path, it will be at the front of the queue
                new_distance = current_distance + distance
                heapq.heappush(priority_queue, (new_distance, neighbour))

        return visited

