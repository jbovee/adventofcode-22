get_input = lambda: [l.strip('\n') for l in open('input','r+',encoding='utf-8').readlines()]

def main():
    assignments = get_input()
    total = 0
    for assignment in assignments:
        elfx,elfy = assignment.split(',')
        x1,x2 = map(lambda x: int(x), elfx.split('-'))
        y1,y2 = map(lambda y: int(y), elfy.split('-'))
        if (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2):
            total += 1
    print('Total assignments fully overlapped: {}'.format(total))

if __name__ == '__main__':
    main()