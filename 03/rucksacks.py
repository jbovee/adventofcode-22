def priority(c):
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1

def get_input():
    with open('input','r+',encoding='utf-8') as f:
        return [l.strip('\n') for l in f.readlines()]

def main():
    rucksacks = get_input()
    # part 1
    total = 0
    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        pocket1,pocket2 = rucksack[:mid],rucksack[mid:]
        common = set(pocket1).intersection(set(pocket2))
        total = total + priority(list(common)[0])
    print('Total priority: {}'.format(total))

    # part 2
    total_2 = 0
    for r in range(0,len(rucksacks),3):
        r1,r2,r3 = rucksacks[r:r+3]
        common = set(r1).intersection(set(r2),set(r3))
        total_2 = total_2 + priority(list(common)[0])
    print('Total priority: {}'.format(total_2))

if __name__ == '__main__':
    main()