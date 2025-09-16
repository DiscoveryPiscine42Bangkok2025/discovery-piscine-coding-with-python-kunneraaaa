import sys

if len(sys.argv) <= 2:
    print("none")
else:
    i = -1
    for _ in range(len(sys.argv) - 1):
        print(sys.argv[i])
        i -= 1