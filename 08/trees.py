get_input = lambda filename: [[int(x) for x in [*l.strip('\n')]] for l in open(filename,'r+',encoding='utf-8').readlines()]

def main():
    forestH = get_input('input')
    # mirror the forest for easier slicing; mirrored diagonally from top left to bottom right
    forestV = [[row[i] for row in forestH] for i in range(len(forestH[0]))]
    visibleTrees = ((len(forestH) - 1) * 2) + ((len(forestH[0]) - 1) * 2)
    bestScore = 0
    for i in range(1,len(forestH)-1):
        for j in range(1,len(forestH[0])-1):
            currentTree = forestH[i][j]
            # part 1
            #  left                                              right                                               top                                               bottom
            if all(h < currentTree for h in forestH[i][:j]) or all(h < currentTree for h in forestH[i][j+1:]) or all(h < currentTree for h in forestV[j][:i]) or all(h < currentTree for h in forestV[j][i+1:]):
                visibleTrees += 1
            # part 2
            # left
            leftOfTree = forestH[i][:j]
            leftView = list(filter(lambda x: x >= currentTree,leftOfTree))
            leftScore = leftOfTree[::-1].index(leftView[-1]) + 1 if leftView else len(leftOfTree)
            # right
            rightOfTree = forestH[i][j+1:]
            rightView = list(filter(lambda x: x >= currentTree,rightOfTree))
            rightScore = rightOfTree.index(rightView[0]) + 1 if rightView else len(rightOfTree)
            # top
            topOfTree = forestV[j][:i]
            topView = list(filter(lambda x: x >= currentTree,topOfTree))
            topScore = topOfTree[::-1].index(topView[-1]) + 1 if topView else len(topOfTree)
            # bottom
            botOfTree = forestV[j][i+1:]
            botView = list(filter(lambda x: x >= currentTree,botOfTree))
            botScore = botOfTree.index(botView[0]) + 1 if botView else len(botOfTree)

            currentScore = leftScore * rightScore * topScore * botScore
            if currentScore > bestScore:
                bestScore = currentScore
    print('Total visible trees: {}'.format(visibleTrees))
    print('Best view score: {}'.format(bestScore))

if __name__ == '__main__':
    main()