get_input = lambda: [l.strip('\n') for l in open('input','r+',encoding='utf-8').readlines()]

def find_set_of_length(target,datastream):
    buffer = []
    for c in range(len(datastream)):
        buffer.append(datastream[c])
        if len(buffer) > target:
            buffer = buffer[1:]
        if len(list(set(buffer))) == target:
            return(c+1)
    return(-1)

def main():
    datastreams = get_input()
    for datastream in datastreams:
        # part 1
        start = find_set_of_length(4,datastream)
        if start != -1:
            print('After character: {}'.format(start))
        else:
            print('Failed to find set of length 4')
        # part 2
        message = find_set_of_length(14,datastream)
        if message != -1:
            print('After character: {}'.format(message))
        else:
            print('Failed to find set of length 14')

if __name__ == '__main__':
    main()