from __future__ import annotations
from os import path
from typing import List

class Node():
    def __init__(self: Node) -> None:
        self.position = {
            'x': 0,
            'y': 0
        }
        self.history = [(0, 0)]
        
    def get_position(self: Node) -> tuple:
        return (self.position.get('x'), self.position.get('y'))
    
    def set_position(self: Node, x: int, y: int) -> None:
        self.position.update({'x': x, 'y': y})
        
    def update_history(self: Node, x: int, y: int) -> None:
        self.history.append((x, y)) # type: ignore        
        
    def count_unique_positions(self: Node) -> int:
        return len(list(set(self.history)))

class Rope():
    def __init__(self: Rope, node_count: int) -> None:
        self.nodes = []
        for _ in range(node_count):
            node = Node()
            self.nodes.append(node)
    
    def get_head(self: Rope) -> Node:
        return self.nodes[0]
    
    def get_tail(self: Rope) -> Node:
        return self.nodes[-1]
    
    def move(self: Rope, instruction: tuple) -> None:
        direction, amount = instruction
        if direction == 'R':
            for _ in range(amount): self.step_right()
            return
        if direction == 'L':
            for _ in range(amount): self.step_left()
            return
        if direction == 'U':
            for _ in range(amount): self.step_up()
            return
        if direction == 'D':
            for _ in range(amount): self.step_down()
            return
            
        raise Exception(f'Could not process a direction from the given input set. Found: {direction} {amount}')
    
    def step_right(self: Rope) -> None:
        head = self.get_head()
        x, y = head.get_position()
        x += 1
        head.set_position(x, y)
        head.update_history(x, y)
        self.process_nodes()
    
    def step_left(self: Rope) -> None:
        head = self.get_head()
        x, y = head.get_position()
        x -= 1
        head.set_position(x, y)
        head.update_history(x, y)
        self.process_nodes()
    
    def step_up(self: Rope) -> None:
        head = self.get_head()
        x, y = head.get_position()
        y += 1
        head.set_position(x, y)
        head.update_history(x, y)
        self.process_nodes()
    
    def step_down(self: Rope) -> None:
        head = self.get_head()
        x, y = head.get_position()
        y -= 1
        head.set_position(x, y)
        head.update_history(x, y)
        self.process_nodes()
        
    def process_nodes(self: Rope):
        last = self.get_head()
        # We already moved the head so we can skip it when processing nodes
        for node in self.nodes[1:]:
            last_x, last_y = last.get_position()
            x, y = node.get_position()
            
            if self.is_adjacent(last, node):
                node.update_history(x, y)
                last = node
                continue
            
            x_offset = self.find_positional_change(last_x - x)
            y_offset = self.find_positional_change(last_y - y)
            x += x_offset
            y += y_offset
            node.set_position(x, y)
            node.update_history(x, y)
            last = node
        
    def is_adjacent(self: Rope, current: Node, last: Node) -> bool:
        last_x, last_y = last.get_position()
        x, y = current.get_position()
        delta_x = abs(last_x - x)
        delta_y = abs(last_y - y)
        
        return delta_x <= 1 and delta_y <= 1
    
    def find_positional_change(self: Rope, distance: int) -> int:
        if distance == 0: return 0 # Stay put
        elif distance > 0: return 1 # Move up and/or right
        else: return -1 # Move down and/or left
               
def handle_input() -> List[tuple]:
    instructions = []
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    with open(filename, 'r') as f:
        for line in f:
            instruction = line.split()
            instructions.append((instruction[0], int(instruction[1])))
    return instructions

def problem_1(instructions: List[tuple]) -> None:
    rope = Rope(2)
    for instruction in instructions:
        rope.move(instruction)
    print(f'Part 1 solution: {rope.get_tail().count_unique_positions()}')

def problem_2(instructions: List[tuple]) -> None:
    rope = Rope(10)
    for instruction in instructions:
        rope.move(instruction)

    print(f'Part 2 solution: {rope.get_tail().count_unique_positions()}')

instructions = handle_input()
problem_1(instructions)
problem_2(instructions)

