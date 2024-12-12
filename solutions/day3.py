def first():
    with open("day3.txt", 'r') as f:
        lines = f.readlines()
        res = 0

        for line in lines:
            n = len(line)

            i = 0
            while i < n:
                if line[i] == 'm':
                    if i + 4 < n:
                        # mul(
                        if line[i:i+4] == "mul(":
                            first = []
                            second = []

                            j = i + 4
                            while line[j] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                                first.append(line[j])
                                j += 1

                            if line[j] == ',':
                                j += 1
                            else:
                                i = j
                                continue

                            while line[j] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                                second.append(line[j])
                                j += 1

                            if line[j] == ')':
                                if first != [] and second != []:
                                    res += int(''.join(first)) * int(''.join(second))

                            i = j

                i += 1

        print(res)

def second():
    with open("day3.txt", 'r') as f:
        lines = f.readlines()
        res = 0
        enabled = True

        for line in lines:
            n = len(line)
            i = 0

            while i < n:
                if line[i] == 'm':
                    if i + 4 < n:
                        # mul(
                        if line[i:i+4] == "mul(":
                            first = []
                            second = []

                            j = i + 4
                            while line[j] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                                first.append(line[j])
                                j += 1

                            if line[j] == ',':
                                j += 1
                            else:
                                i = j
                                continue

                            while line[j] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                                second.append(line[j])
                                j += 1

                            if line[j] == ')':
                                if enabled and first != [] and second != []:
                                    print(f"{int(''.join(first))},{int(''.join(second))}")
                                    res += int(''.join(first)) * int(''.join(second))

                            i = j
                elif line[i] == 'd':
                    if enabled:
                        # don't()
                        if i + 7 < n:
                            if line[i:i+7] == "don't()":
                                enabled = False
                                i += 6
                    else:
                        # do()
                        if i + 4 < n:
                            if line[i:i+4] == "do()":
                                enabled = True
                                i += 3
                i += 1

        print(res)

if __name__ == "__main__":
    first()
    second()
