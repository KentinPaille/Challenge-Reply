for i in range(int(input())):
    size, nb_colour, total_gem = map(int, input().split())
    maps = [["." for x in range(size)] for y in range(size)]
    for j in range(total_gem):
        x, y, colour = input().split()
        maps[int(y)][int(x)] = colour

    for y in range(size):
        for x in range(size):
            print(maps[x][y], end=" ")
        print()

    # find all squares where i have all the gems with different colours
    # find the smallest square
    # find the biggest square

    squares = [0, 0, 0, 0, 10000000]
    pos = [0, 0, 0, 0]
    gems = []
    for y in range(size):
        for x in range(size):
            print("y, x :", y, x)
            quitt=0
            for i in range(x, size):
                for j in range(y, size):
                    
                    print("y, x, i, j :", y, x, i, j)
                    

                    if maps[j][i] not in gems and maps[j][i] != ".":
                        if len(gems) == 0:
                            pos[0] = i
                            pos[1] = j
                           
                        gems.append(maps[j][i])
                        print("new gem :", maps[j][i], i, j)
                    if len(gems) == nb_colour:
                        print("enttre")
                        if (i - pos[0]) * (j - pos[1]) < squares[4]:
                            print("entre")
                            squares[0] = pos[0]
                            squares[1] = pos[1]
                            squares[2] = i
                            squares[3] = j
                            squares[4] = (i - pos[0]) * (j - pos[1])
                            quitt=1
                        break
                if quitt==1:
                    break
                
            gems = []
            pos = [0, 0, 0, 0]
            break
        break
            

    print("Case #{}: {} {} {} {} {}".format(i + 1, squares[0], squares[1], squares[2], squares[3], squares[4]))
