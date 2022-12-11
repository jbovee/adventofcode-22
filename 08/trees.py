get_input = lambda filename: [[int(x) for x in [*l.strip('\n')]] for l in open(filename,'r+',encoding='utf-8').readlines()]

def main():
    forestH = get_input('input')
    # mirror the forest for easier slicing; mirrored diagonally from top left to bottom right
    forestV = [[row[i] for row in forestH] for i in range(len(forestH[0]))]
    visibleTrees = ((len(forestH) - 1) * 2) + ((len(forestH[0]) - 1) * 2)
    for i in range(1,len(forestH)-1):
        for j in range(1,len(forestH[0])-1):
            #  left                                              right                                               top                                               bottom
            if all(h < forestH[i][j] for h in forestH[i][:j]) or all(h < forestH[i][j] for h in forestH[i][j+1:]) or all(h < forestV[j][i] for h in forestV[j][:i]) or all(h < forestV[j][i] for h in forestV[j][i+1:]):
                visibleTrees += 1
    print('Total visible trees: {}'.format(visibleTrees))

if __name__ == '__main__':
    main()