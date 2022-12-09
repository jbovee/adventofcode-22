get_input = lambda: [l.strip('\n') for l in open('input','r+',encoding='utf-8').readlines()]

blank_array = lambda n: [[-1] for x in range(0,n)]

instrToNums = lambda instr: [int(i) for i in [instr.split()[1],instr.split()[3],instr.split()[5]]]

def main():
    data = get_input()
    stacksRaw = data[:data.index('')-1]
    numStacks = int(data[data.index('')-1].split()[-1])
    # parse numbers from instructions [amount, src, dst]
    instrsRaw = data[data.index('')+1:]
    instrs = list(map(instrToNums, instrsRaw))
    # convert vertical stacks into horizontal lists
    stacksH = blank_array(numStacks)
    for l in range(0,len(stacksRaw)):
        layer = stacksRaw[::-1][l]
        for i in range(1,numStacks+1):
            charPos = i + (3 * (i - 1))
            if layer[charPos] != ' ':
                if stacksH[i-1] == [-1]:
                    stacksH[i-1] = [layer[charPos]]
                else:
                    stacksH[i-1].append(layer[charPos])
    # execute instructions on lists
    for instr in instrs:
        amt,src,dst = instr
        for _ in range(amt):
            stacksH[dst-1].append(stacksH[src-1][-1])
            stacksH[src-1].pop()

    print(''.join([stack[-1] for stack in stacksH]))

if __name__ == '__main__':
    main()