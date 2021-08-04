"""a program that prints out a multiplication table for the numbers 1 through 9"""


def multiplicationTable(size=10,line_space=7):
    """Prints a multiplication table. Default size is 10 and line spacing is 7"""
    for column in range(1,size+1):
        row = ''
        for i in range(1, 11):
            if i*column > 9:
                row += str(i*column) + ' '*( (line_space+1) - len(str(i*column)) )
                continue
            row += str(i*column)+ ' '*line_space
        print(row)



multiplicationTable()