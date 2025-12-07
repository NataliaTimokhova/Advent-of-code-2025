# day 1. task 1 of Advent of Code 2025

def process_instructions(file_path):
    with open(file_path, 'r') as f:
        
        i = 50
        n = 0
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]      # 'R' or 'L'
            steps = int(line[1:])


            if direction == 'R':
                i= (i+steps)%100
            else:  # direction == 'L'
                i= (i - steps)%100
                
            if i == 0:
                n += 1

        print(n)


process_instructions(file_path = 'adventofcode_2025/1_input.txt')
