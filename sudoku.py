import csv, random
#import pandas as pd

#--------------------------DONE------------------------------------
# open csv file, read sudocus and solutions
file = open(r"C:\Users\stsir\OneDrive\Υπολογιστής\sudoku.csv")
reader = csv.reader(file)
sudoku = []
solutions = []

# create lists with sudokus and solutions
for row in reader:
    sudoku.append(row[0])
    solutions.append(row[1])
file.close()
#--------------------------FOR TESTING------------------------------------

# display all sudokus
# for s in sudoku:
#     for i in range(0,8):
#         print(s[9*i:9*i+9])

#--------------------------DONE------------------------------------
# get a random sudoku
n = random.randint(0, len(sudoku))
print("The selected sudoku is number: ", n)
for i in range(0,8):
        print(sudoku[n][9*i:9*i+9])
#--------------------------------------------------------------

