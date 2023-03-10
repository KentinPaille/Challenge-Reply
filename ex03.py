for u in range(int(input())):
    width, height, nb_flowers, nb_grounds = map(int, input().split())
    pos_grounds = [list(map(int, input().split())) for _ in range(nb_grounds)]
    field = [[1 for x in range(width)] for y in range(height)]
    for x, y in pos_grounds:
        field[y][x] = 0

    
    pos = [[0, 0]]
    res = [0, 0]
    for x in range(nb_flowers):
        max_dist = 0
        for i in range(width):
            for j in range(height):
                if (i, j) in pos_grounds or field[j][i] == 2:
                    continue
                dists = [abs(i-x) + abs(j-y) for x, y in pos]
                if max(dists) > max_dist:
                    max_dist = max(dists)
                    res = [i, j]
        pos.append(res)
        field[res[1]][res[0]] = 2

    for i in range(width):
        for j in range(height):
            print(field[j][i], end=" ")
        print()
           
            

    # print the output
    print("Case #{}: {}".format(u + 1, max_dist + 1))

    #for y in range(height):
    #    for x in range(width):
    #        print(field[y][x], end=" ")

        #print()