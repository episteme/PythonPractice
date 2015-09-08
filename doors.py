def main():
    doors = [False] * 100
    for i in range(0, 100):
        for j in range(0, 100):
            if ((j + 1) % (i + 1) == 0):
                doors[j] = not doors[j]
    print_array(doors)

def print_array(a):
    for i in range(0, len(a)):
        print str(i+1) + ": " + str(a[i])

main()
