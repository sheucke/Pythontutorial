with open('Myfile.txt') as f:

    newList = []
    for line in f.readlines():
        if line[-1] == '\n':
            newList.append(line[:-1])
        else:
            newList.append(line)

    print(newList)

    for line in f.readlines():
        newList.append(line.strip())

    print(newList)
