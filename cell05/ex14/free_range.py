import sys

if len(sys.argv) != 3:
    print("none")
else:
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2]) + 1
    print(list(range(number1, number2)))