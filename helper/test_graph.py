from unittest import TestCase
from helper.graph import Graph

__author__ = 'rain'

import heapq

graph = {
    'start': {'00': -3},
    '00': {'10': -7, '11': -4},
    '10': {'20': -2, '21': -4},
    '11': {'21': -4, '22': -6},
    '20': {'30': -8, '31': -5},
    '21': {'31': -5, '32': -9},
    '22': {'32': -9, '33': -3},
}



class TestGraph(TestCase):
    def test_dijsktra(self):
        graph = Graph()
        graph.add_node("start")
        graph.add_node("00")
        graph.add_node("10")
        graph.add_node("11")
        graph.add_node("20")
        graph.add_node("21")
        graph.add_node("22")
        graph.add_node("30")
        graph.add_node("31")
        graph.add_node("32")
        graph.add_node("33")

        graph.add_edge("start", "00", -3)

        graph.add_edge('00', '10', -7)
        graph.add_edge('10', '20', -2)
        graph.add_edge('11', '21', -4)
        graph.add_edge('20', '30', -8)
        graph.add_edge('21', '31', -5)
        graph.add_edge('22', '32', -9)
        graph.add_edge('00', '11', -4)
        graph.add_edge('10', '21', -4)
        graph.add_edge('11', '22', -6)
        graph.add_edge('20', '31', -5)
        graph.add_edge('21', '32', -9)
        graph.add_edge('22', '33', -3)

        visited = graph.dijkstra("start")
        print "hi"

