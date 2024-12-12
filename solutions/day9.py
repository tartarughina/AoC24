def parse():
    disk = []
    id = 0

    with open('../inputs/9.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            file = True


            for c in line.strip():
                if file:
                    for _ in range(int(c)):
                        disk.append(id)

                    file = False
                    id += 1
                else:
                    for _ in range(int(c)):
                        disk.append(-1)

                    file = True

    return disk, id - 1


def checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == -1:
            continue

        checksum += i * disk[i]

    return checksum


def first(disk):
    l = 0
    r = len(disk) - 1

    while l < r:
        if disk[l] != -1:
            l += 1
        elif disk[r] == -1:
            r -= 1
        else:
            disk[l], disk[r] = disk[r], disk[l]
            l += 1
            r -= 1

    return checksum(disk)

# Beautiful wrong solution
# def second(disk):
#     l = 0
#     r = len(disk) - 1

#     while l < r:
#         while disk[l] != -1:
#             l += 1

#         f_start = l

#         while disk[l] == -1:
#             l += 1

#         avail = l - f_start

#         size = avail + 1
#         while size > avail:
#             while disk[r] == -1:
#                 r -= 1

#             block_id = disk[r]
#             m_start = r
#             while disk[r] == block_id:
#                 r -= 1

#             size = m_start - r

#             if avail >= size:
#                 disk[f_start:f_start + size], disk[m_start-size+1:m_start+1] = disk[m_start-size+1:m_start+1], disk[f_start:f_start + size]
#                 l = f_start + size

#     return checksum(disk)
#

def second(disk, max_id):
    r = len(disk) - 1
    block_id = max_id

    while r >= 0:
        while disk[r] != block_id:
            r -= 1

        m_start = r

        while disk[r] == block_id:
            r -= 1

        size = m_start - r

        l = 0
        avail = 0

        while avail < size and l < r:
            while disk[l] != -1 and l < r:
                l += 1

            f_start = l

            while disk[l] == -1 and l < r:
                l += 1

            avail = l - f_start

            if avail >= size:
                disk[f_start:f_start + size], disk[r+1:m_start+1] = disk[r+1:m_start+1], disk[f_start:f_start + size]

        block_id -= 1

    return checksum(disk)

if __name__ == "__main__":
    disk, max_id = parse()

    print(first(disk[:]))
    print(second(disk[:], max_id))
    # print(second([0,0,-1,-1,-1,1,1,1,-1,-1,-1,2,-1,-1,-1,3,3,3,-1,4,4,-1,5,5,5,5,-1,6,6,6,6,-1,7,7,7,-1,8,8,8,8,9,9], 9))
