"""
Pseudo reference from wikipedia. See: https://en.wikipedia.org/wiki/A*_search_algorithm
function reconstruct_path(cameFrom, current)
    total_path := {current}
    while current in cameFrom.Keys:
        current := cameFrom[current]
        total_path.prepend(current)
    return total_path

function A_Star(start, goal, h)
    // The set of discovered nodes that may need to be (re-)expanded.
    // Initially, only the start node is known.
    // This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet := {start}

    // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    // to n currently known.
    cameFrom := an empty map

    // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore := map with default value of Infinity
    gScore[start] := 0

    // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    // how cheap a path could be from start to finish if it goes through n.
    fScore := map with default value of Infinity
    fScore[start] := h(start)

    while openSet is not empty
        // This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        current := the node in openSet having the lowest fScore[] value
        if current = goal
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        for each neighbor of current
            // d(current,neighbor) is the weight of the edge from current to neighbor
            // tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore := gScore[current] + d(current, neighbor)
            if tentative_gScore < gScore[neighbor]
                // This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] := current
                gScore[neighbor] := tentative_gScore
                fScore[neighbor] := tentative_gScore + h(neighbor)
                if neighbor not in openSet
                    openSet.add(neighbor)

    // Open set is empty but goal was never reached
    return failure

"""

from __future__ import annotations
import heapq
from os import path
from timeit import default_timer as timer

LOWER_CASE_OFFSET = 96

class Node():
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.f, self.g, self.h = 0, 0, 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    def __lt__(self, other):
      return self.f < other.f
    
    def __gt__(self, other):
      return self.f > other.f

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path

def astar(maze, start, end):
    """ An attempt at A* pathfinding """
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    neighbours = ((0, -1), (0, 1), (-1, 0), (1, 0))

    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Queue skyfall intro
        if current_node == end_node:
            return return_path(current_node)

        children = []
        for new_position in neighbours:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            
            # Check bounds
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Check elevation
            c_x, c_y = current_node.position[0], current_node.position[1]
            n_x, n_y = node_position[0], node_position[1]

            if maze[n_x][n_y] - maze[c_x][c_y] > 1:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

            for child in children:
                # Check closed list
                if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                    continue

                child.g = current_node.g + (((child.position[0] - child.parent.position[0]) ** 2) + ((child.position[1] - child.parent.position[1]) ** 2))**0.5
                child.h = (((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))**0.5
                child.f = child.g + child.h

                # Check open list
                if child in open_list: 
                    idx = open_list.index(child) 
                    if child.g < open_list[idx].g:
                        # update the node in the open list
                        open_list[idx].g = child.g
                        open_list[idx].f = child.f
                        open_list[idx].h = child.h
                else:
                    heapq.heappush(open_list, child)

    print("Couldn't get a path :(")
    return None
        

def find_start_position(instructions):
    for i, row in enumerate(instructions):
        for j, col in enumerate(row):
            if instructions[i][j] == 'S':
                return (i, j)

    raise IndexError('Could not determine start position')


def find_end_position(instructions):
    for i, row in enumerate(instructions):
        for j, col in enumerate(row):
            if instructions[i][j] == 'E':
                return (i, j)

    raise IndexError('Could not determine end position')


def handle_input():
    instructions = []
    costs = []
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    with open(filename, 'r') as f:
        for line in f:
            instructions.append(line.rstrip('\n'))

    for row in instructions:
        costs.append([ord(x) - LOWER_CASE_OFFSET for x in row])

    start = find_start_position(instructions)
    costs[start[0]][start[1]] = 0
    end = find_end_position(instructions)
    costs[end[0]][end[1]] = 27

    return (costs, start, end)


maze, start, end = handle_input()
start_time = timer()
print(f'A* Solution 1: {len(astar(maze, start, end)) - 1}')
end_time = timer()
print(f' Done in {end_time - start_time}s')