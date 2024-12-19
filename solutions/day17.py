registers = {
    '4': 0,
    '5': 0,
    '6': 0
}


def get_operand(op):
    if op in ('0', '1', '2', '3'):
        return int(op)
    else:
        return registers[op]


def get_val_for_reg(line):
    return int(line.split(': ')[1])


def parse():
    program = []

    with open('../inputs/17.txt', 'r') as f:
        registers['4'] = get_val_for_reg(f.readline().strip())
        registers['5'] = get_val_for_reg(f.readline().strip())
        registers['6'] = get_val_for_reg(f.readline().strip())

        f.readline()

        program = f.readline().strip().split(': ')[1].split(',')

    return program


def first(program, threshold = 100):
    pt = 0
    out = []

    while pt < len(program):
        operand = program[pt + 1]

        if program[pt] == '0':
            registers['4'] = int(registers['4'] / (2 ** get_operand(operand)))
        elif program[pt] == '1':
            registers['5'] = registers['5'] ^ int(operand)
        elif program[pt] == '2':
            registers['5'] = get_operand(operand) % 8
        elif program[pt] == '3':
            if registers['4'] != 0:
                pt = int(operand)
                continue
        elif program[pt] == '4':
            registers['5'] = registers['5'] ^ registers['6']
        elif program[pt] == '5':
            out.append(str(get_operand(operand) % 8))

            if len(out) > threshold:
                return out

        elif program[pt] == '6':
            registers['5'] = int(registers['4'] / (2 ** get_operand(operand)))
        elif program[pt] == '7':
            registers['6'] = int(registers['4'] / (2 ** get_operand(operand)))

        pt += 2

    return out


def reset(val):
    registers['4'] = val
    registers['5'] = 0
    registers['6'] = 0


def second(program):
    val = -1
    out = None

    while out != program:
        val += 1
        reset(val)

        out = first(program, threshold=len(program))

    return val


if __name__ == "__main__":
    program = parse()

    print(','.join(first(program)))
    print(second(program))
