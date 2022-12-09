from os import path

class Rope:
    head_seen = []
    tail_seen = []
    head = (8, 8)
    tail = (8, 8)

    def move_up(self, y: int):
        pass

    def move_down(self, y: int):
        pass

    def move_left(self, x: int):
        cur_x, cur_y = self.head
        for d in range(cur_x, cur_x - x - 1, -1):
            self.head = (d, cur_y)
            self.tail = self.determine_tail_from_move(self.tail, self.head)
            self.head_seen.append(self.head)
            self.tail_seen.append(self.tail)

    def move_right(self, x: int):
        cur_x, cur_y = self.head
        for d in range(cur_x, cur_x + x + 1):
            self.head = (d, cur_y)
            self.tail = self.determine_tail_from_move(self.tail, self.head)
            self.head_seen.append(self.head)
            self.tail_seen.append(self.tail)

    def move(self, dir: str, amount: int):
        if dir == 'R':
            self.move_right(amount)
        if dir == 'L':
            self.move_left(amount)
        if dir == 'U':
            self.move_up(amount)
        if dir == 'D':
            self.move_down(amount)

    def determine_tail_from_move(self, tail: tuple, new_head: tuple) -> tuple:
        tail_x, tail_y = tail
        head_x, head_y = new_head
        print(f'Head: {head_x}')
        print(f'Tail: {tail_x}')

        # Right t least doesn't work
        if head_y > tail_y and tail_x == head_x: return (head_x, head_y - 1) # Handle up
        if head_y < tail_y and tail_x == head_x: return (head_x, head_y + 1) # Handle down
        if head_x > tail_x and tail_y == head_y: return (head_x - 1, head_y) # Handle right
        if head_x < tail_x and tail_x == head_y: return (head_x + 1, head_y) # Handle left

        # Handle diagonal movement
        return (tail_x, tail_y) # Tail doesn't move until head moves again

def handle_input():
    instructions = []
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, 'in.txt')
    with open(filename, 'r') as f:
        for line in f:
            instruction = line.split()
            instructions.append((instruction[0], int(instruction[1])))

    return instructions

def problem1(instructions):
    rope = Rope()
    for instruction in instructions:
        (direction, amount) = instruction
        rope.move(direction, amount)

    print(rope.head_seen)
    print(rope.tail_seen)


instructions = handle_input()
problem1(instructions)