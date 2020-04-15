if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")
        list = x[0]
        if list == 'append':
            result.append(int(x[1]))
        if list == 'print':
            print(result)
        if list == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if list == 'reverse':
            result = result[::-1]
        if list == 'pop':
            result.pop()
        if list == 'sort':
            result = sorted(result)
        if list == 'remove':
            result.remove(int(x[1]))
