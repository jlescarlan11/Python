"""
nested loop =   The "inner loop" will finish all of its iiterations before
                finishing one iteration of the "outer loop"
"""

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")

for _ in range(rows):
    for _ in range(columns):
        print(symbol, end='')
    print()
