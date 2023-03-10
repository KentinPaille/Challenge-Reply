def nb_targets(maps)->int:
    count = 0
    for i in range(len(maps)):
        for j in range(len(maps)):
            if maps[i][j] != 0:
                count += 1
    return count

for u in range(int(input())):
    witdh, nb_target = map(int, input().split())
    maps = [[0 for i in range(witdh)] for i in range(witdh)]
    pos = [0, 0]
    last_pos = [-1, -1]
    dist = 0
    last_dist = 0
    total_dist = 0
    loop = True
    for i in range(nb_target):
        x, y, z = map(int, input().split())
        if i == 0:
            pos[0] = x
            pos[1] = y
        maps[x][y] = z

    for i in range(witdh):
            print(maps[i])
    print(pos, last_pos, last_dist)
    while loop:
        nearest = 1000000
        maps[pos[0]][pos[1]] -= 1
        last_pos = pos
        for i in range(witdh):
            print(maps[i])
        if (test = nb_targets(maps) == 0):
            loop = False
        
        for i in range(witdh):
            for j in range(witdh):
                test = nb_targets(maps)
                if maps[j][i] != 0 and [j, i] != pos and ([j, i] != last_pos or test == 1):
                    dist = abs(pos[0] - j) + abs(pos[1] - i)
                    if dist < nearest:
                        pos = [j, i]
                        last_dist = dist
                        nearest = dist
                    elif dist == nearest:
                        if j < pos[0]:
                            pos = [j, i]
                            last_dist = dist
                            nearest = dist
                        elif j == pos[0] and i < pos[1]:
                            pos = [j, i]
                            last_dist = dist
                            nearest = dist
        
        print(pos, last_pos, last_dist)
        total_dist += last_dist
    print("Case #" + str(u + 1) + ": " + str(total_dist))
