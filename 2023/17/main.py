from __future__ import  annotations

import sys

from dataclasses import dataclass, field
from queue import PriorityQueue
from copy import deepcopy


@dataclass(order=True)
class Node:
    pos: tuple[int, int]=field(compare=False)
    heat_loss: int
    previous: Node|None=field(compare=False)
    x_count: int=field(compare=False)
    y_count: int=field(compare=False)
    depth: int=field(compare=False)

    def get_adjacent(self, graph):
        x, y   = self.pos
        px, py = self.previous.pos if self.previous is not None else (-1, -1)

        nodes = []

        if (y > 0 and py != y-1 and self.y_count != 3):
            nodes.append(Node((x, y-1), self.heat_loss + graph[y-1][x], self, 0, self.y_count+1, self.depth+1))
        if (x < len(graph[0])-1 and px != x+1 and self.x_count != 3):
            nodes.append(Node((x+1, y), self.heat_loss + graph[y][x+1], self, self.x_count+1,0, self.depth+1))
        if (y < len(graph)-1 and py != y+1 and self.y_count != 3):
            nodes.append(Node((x, y+1), self.heat_loss + graph[y+1][x], self, 0, self.y_count+1, self.depth+1))
        if (x > 0 and px != x-1 and self.x_count != 3):
            nodes.append(Node((x-1, y), self.heat_loss + graph[y][x-1], self, self.x_count+1,0, self.depth+1))

        return nodes

@dataclass(order=True)
class UltraNode:
    pos: tuple[int, int]=field(compare=False)
    heat_loss: int
    previous: UltraNode|None=field(compare=False)
    x_count: int=field(compare=False)
    y_count: int=field(compare=False)
    depth: int=field(compare=False)

    def get_adjacent(self, graph):
        x, y   = self.pos
        px, py = self.previous.pos if self.previous is not None else (-1, -1)

        if self.x_count > 0 and self.x_count < 4:
            if x > 0 and px != x-1:
                return [UltraNode((x-1, y), self.heat_loss + graph[y][x-1], self, self.x_count+1,0, self.depth+1)]
            elif x < len(graph[0])-1 and px != x+1:
                if x+1 == len(graph[0])-1 and self.x_count+1 < 4:
                    return []
                return [UltraNode((x+1, y), self.heat_loss + graph[y][x+1], self, self.x_count+1,0, self.depth+1)]
            else:
                return []
        elif self.y_count > 0 and self.y_count < 4:
            if y > 0 and py != y-1:
                return [UltraNode((x, y-1), self.heat_loss + graph[y-1][x], self, 0, self.y_count+1, self.depth+1)]
            elif y < len(graph)-1 and py != y+1:
                if y+1 == len(graph)-1 and self.y_count+1 < 4:
                    return []
                return [UltraNode((x, y+1), self.heat_loss + graph[y+1][x], self, 0, self.y_count+1, self.depth+1)]
            else:
                return []
        else:
            nodes = []

            if (y > 0 and py != y-1 and self.y_count != 10):
                nodes.append(UltraNode((x, y-1), self.heat_loss + graph[y-1][x], self, 0, self.y_count+1, self.depth+1))
            if (x < len(graph[0])-1 and px != x+1 and self.x_count != 10):
                if x+1 != len(graph[0])-1 or self.x_count > 0:
                    nodes.append(UltraNode((x+1, y), self.heat_loss + graph[y][x+1], self, self.x_count+1,0, self.depth+1))
            if (y < len(graph)-1 and py != y+1 and self.y_count != 10):
                if y+1 != len(graph)-1 or self.y_count > 0:
                    nodes.append(UltraNode((x, y+1), self.heat_loss + graph[y+1][x], self, 0, self.y_count+1, self.depth+1))
            if (x > 0 and px != x-1 and self.x_count != 10):
                nodes.append(UltraNode((x-1, y), self.heat_loss + graph[y][x-1], self, self.x_count+1,0, self.depth+1))

            return nodes


city = [[int(char) for char in line] for line in map(str.strip,open(sys.argv[1]).readlines())]

def calc_heat_loss(city, seen, ultra=False):
    graph = deepcopy(city)

    pq    = PriorityQueue(-1)
    start = Node((0, 0), 0, None, 0, 0, 0) if not ultra else UltraNode((0, 0), 0, None, 0, 0, 0)

    pq.put_nowait(start)

    while (current := pq.get_nowait()).pos != (len(graph[0])-1, len(graph)-1):
        adjacent_nodes = current.get_adjacent(graph)
        for node in adjacent_nodes:
            key = (node.pos[0], node.pos[1], node.previous.pos[0], node.previous.pos[1], node.x_count, node.y_count)
            if key not in seen:
                pq.put_nowait(node)
                seen.add(key)

    return current.heat_loss

print(calc_heat_loss(city, set()))
print(calc_heat_loss(city, set(), True))
