import sys

parameters = sys.argv[1:]

if not parameters:
    print("none")
else:
    for param in parameters:
        if not param.endswith("ism"):
            print(f"{param}ism")
            