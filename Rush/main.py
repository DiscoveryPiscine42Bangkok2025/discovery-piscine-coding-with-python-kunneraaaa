from checkmate import checkmate

def main():
    # Example 1
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)

    # Example 2
    board = """\
..
.K\
"""
    checkmate(board)

if __name__ == "__main__":
    main()
