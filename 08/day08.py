with open('./input_all.txt') as f:
    instructions = f.readline().strip()
    f.readline()
    mmap = {}
    for line in f:
        line = line.strip()
        start, left_right = line.split(' = ')
        left, right = left_right.strip()[1:-1].split(',')
        start = start.strip()
        left = left.strip()
        right = right.strip()
        mmap[start] = (left, right)

# follow instructions
curr = 'AAA'
target = 'ZZZ'
count = 0

while curr != target:
    for instruction in instructions:
        if instruction == 'L':
            curr = mmap[curr][0]
        else:
            curr = mmap[curr][1]
    count += 1
    if curr == target:
        print(f'Found target after {count} loop through instructions, {count*len(instructions)} steps total')
    
