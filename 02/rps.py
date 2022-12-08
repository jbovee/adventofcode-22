def get_input():
    with open('input','r+',encoding='utf-8') as f:
        data = [l.strip('\n') for l in f.readlines()]
    return data

def main():
    matches = get_input()
    # part 1
    score = 0
    points = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
        }
    for match in matches:
        score = score + points[match]
    print('Total score: {}'.format(score))

    # part 2
    score_2 = 0
    points_2 = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }
    for match in matches:
        score_2 = score_2 + points_2[match]
    print('Total score: {}'.format(score_2))

if __name__ == "__main__":
    main()