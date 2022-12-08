def priority(c):
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1

def get_input():
    with open('input','r+',encoding='utf-8') as f:
        return [l.strip('\n') for l in f.readlines()]

def main():
    rucksacks = get_input()
    total = 0
    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        pocket1,pocket2 = rucksack[:mid],rucksack[mid:]
        common = set(pocket1).intersection(set(pocket2))
        total = total + priority(list(common)[0])
    print('Total priority: {}'.format(total))

if __name__ == '__main__':
    main()