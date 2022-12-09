get_input = lambda: [l.strip('\n') for l in open('input','r+',encoding='utf-8').readlines()]

def main():
    datastreams = get_input()
    for datastream in datastreams:
        latestFour = []
        for c in range(len(datastream)):
            latestFour.append(datastream[c])
            if len(latestFour) > 4:
                latestFour = latestFour[1:]
            if len(list(set(latestFour))) == 4:
                print('After character: {}'.format(c+1))
                break

if __name__ == '__main__':
    main()