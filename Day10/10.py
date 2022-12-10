from __future__ import annotations
import itertools # Hello cheat
from os import path
from typing import List, Iterator

def handle_input():
    instructions = []
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if line[-1].isnumeric():
                instruction = line.split()
                instructions += [(instruction[0], int(instruction[1]))]
            else:
                instructions += [(line, None)]

    return instructions     

def build_cycles(instructions: List[tuple]) -> Iterator:
    x = 1
    cycle = 1
    for instruction, amount in itertools.cycle(instructions):
        if instruction == 'noop':
            yield x, cycle # Yield current values directly
            cycle += 1 # Increment next cycle
        else:
            yield x, cycle # Yield current values directly
            cycle += 1 # Delay by cycle
            yield x, cycle # Honestly this feels like cheating at this point
            cycle += 1
            x += amount

def build_graphics(instructions: List[tuple]) -> dict:
    output = dict()
    for x, cycle in build_cycles(instructions):
        index = cycle - 1
        row = index % 40
        col = index // 40
        
        # Check position, with offsets to both sides since any of the sprite's pixel draws a #
        if row in (x - 1, x, x + 1):
            output[col, row] = '#'
        else:
            output[col, row] = '.'
            
        if index > 240:
            break

    return output
  
def problem_1(instructions: List[tuple]):
    check_cycles = [i for i in range(20, 221, 40)] # end exclusive
    total = 0 
    end_limit = check_cycles[-1] # Learned infinite recursion the hard way again...
    for x, cycle in build_cycles(instructions):
        if cycle in check_cycles:
            total += cycle * x
        if cycle > end_limit:
            print(total)
            return total
        
def problem_2(instructions: List[tuple]):
    output = build_graphics(instructions)
    grid_height = 240 // 40
    grid_width = 40
    for x in range(0, grid_height):
        for y in range(0, grid_width):
            print(output[x, y], end='')
        print() # Print newline since we're going to next row
    
    
instructions = handle_input()
problem_1(instructions)
problem_2(instructions)
        