for z in range(int(input())):
    nb_people, nb_day = map(int, input().split())
    a = [[0 for x in range(nb_day)] for y in range(nb_people)]
    list = [int(x) for x in input().split()]
    for j in range(nb_people):
        for k in range( nb_day):
            if k == 0:
                a[j][k] = 1
            elif k % list[j] == 0:
                a[j][k] = 1
    max = 0
    for i in range(nb_day):
        count = 0
        for j in range(nb_people):
            if (a[j][i] == 1):
                count += 1
        if count == nb_people:
            max += 1
    print("Case #" + str(z + 1) + ": " + str(max))