get_input = lambda: [l.strip('\n') for l in open('input','r+',encoding='utf-8').readlines()]

def parse_data(data):
    elves,start,end = [],0,0
    while start < len(data):
        try:
            end = data.index('',start)
        except ValueError:
            end = len(data)
        finally:
            elves.append([int(x) for x in data[start:end]])
            start = end + 1
    return elves

def main():
    data = get_input()
    elves = parse_data(data)
    # part 1
    sortedElves = sorted([sum(elf) for elf in elves], reverse=True)
    biggestElf = sortedElves[0]
    print('Top elf: {}'.format(biggestElf))

    # part 2
    topThree = sum(sortedElves[:3])
    print('Top three sum: {}'.format(topThree))

if __name__ == '__main__':
    main()