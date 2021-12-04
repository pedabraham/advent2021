from collections import defaultdict
boards = []
sumas = []
regs = []

with open('input4') as input4:
    numbers = input4.readline()
    numbers = numbers.strip()
    numbers = numbers.split(',')
    i = 0
    while True:
        line = input4.readline()
        if not line:
            break
        board = {}
        boards.append(board)
        regs.append({'x':defaultdict(list),'y':defaultdict(list)})
        suma = 0
        for row_i in range(5):
            row = input4.readline()
            row = row.strip()
            row = row.split()
            col_i = 0
            for element in row:
                element = int(element)
                board[element] = (col_i,row_i)
                col_i += 1
                suma += element
        sumas.append(suma)
        i += 1
n_found = False
winners = []
for num in numbers:
    num = int(num)
    for i in range(len(boards)):
        board = boards[i]
        reg = regs[i]
        location = board.get(num)
        if not location:
            continue
        x = location[0]
        y = location[1]
        reg['x'][x].append(num)
        reg['y'][y].append(num)
        sumas[i] -= num

        if len(reg['x'][x]) == 5:
            if i not in winners:
                print(f'x we have a winner in board {i}')
                print(reg['x'][x])
                print(f'{sumas[i]} * {num} : {sumas[i] * num}')
                n_found = True
                winners.append(i)
        if len(reg['y'][y]) == 5:
            if i not in winners:
                print(f'y we have a winner in board {i}')
                print(reg['y'][y])
                print(f'{sumas[i]} * {num} : {sumas[i] * num}')
                n_found = True
                winners.append(i)
