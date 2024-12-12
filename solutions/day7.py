def parse():
    ret = []

    with open('../inputs/7.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            res, remain = line.split(':')

            vals = remain.strip().split(' ')

            ret.append({'target': int(res), 'nums': list(map(int, vals))})

    return ret


def evaluate(target, nums, running):

    if nums:
        sum = evaluate(target, nums[1:], running + nums[0])
        mul = evaluate(target, nums[1:], running * nums[0])

        return sum or mul

    return running == target

def evaluate_ext(target, nums, running):

    if nums:
        sum = evaluate_ext(target, nums[1:], running + nums[0])
        mul = evaluate_ext(target, nums[1:], running * nums[0])
        concat = evaluate_ext(target, nums[1:], int(str(running) + str(nums[0])))

        return sum or mul or concat

    return running == target

def first(tests):
    running = 0

    for test in tests:
        if evaluate(test['target'], test['nums'][1:], test['nums'][0]):
            running += test['target']

    return running


def second(tests):
    running = 0

    for test in tests:
        if evaluate_ext(test['target'], test['nums'][1:], test['nums'][0]):
            running += test['target']

    return running

if __name__ == "__main__":
    tests = parse()

    print(first(tests))
    print(second(tests))
