def get_input():
    with open('input','r+',encoding='utf-8') as f:
        data = [l.strip('\n') for l in f.readlines()]
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
    elves = get_input()
    biggestElf = max([sum(elf) for elf in elves])
    print(biggestElf)

if __name__ == "__main__":
    main()