# Day 1 – Part Two, Advent of Code 2025

def process_instructions(file_path):
    i = 50   # initial dial position
    n = 0    # number of times the dial points to 0 (on ANY click)

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]      # 'R' or 'L'
            steps = int(line[1:])

            # determine step direction
            if direction == 'R':
                step = 1
            else:  # 'L'
                step = -1

            # rotate the dial ONE CLICK at a time
            for _ in range(steps):
                i = (i + step) % 100
                if i == 0:
                    n += 1

    print(n)


process_instructions(file_path='adventofcode_2025/1_input.txt')

