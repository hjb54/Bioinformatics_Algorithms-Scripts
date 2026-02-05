import sys
import argparse


#function to parse command line arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(
    description="ADD TITLE OF SCRIPT HERE (shows on help -h)")
    parser.add_argument("-i", "--input",
    help="input file",
    required=True)
    parser.add_argument("-o", "--output",
    help="output file",
    required=True)
    return parser.parse_args(args)

#retrieve command line arguments
arguments = check_arg(sys.argv[1:])
infile = arguments.input
outfile = arguments.output
#everything above from class

#open file as read obj, read lines to form a list of lines
with open(infile, 'r') as file:
    lines = file.readlines()
    hold =["" ,""] #list of 2 items, used to seperate the sequences
    i = 0
    for line in lines:
        if line.startswith(">"):
            i = i + 1 #counter to split sequences at ">"
        elif i == 1: #first occurance of ">" is added to index 0- need to do this to work with larger files, cannot be sure that it will read in as expected
            hold[0] += line.strip() #remove whitespace
        else: #second occurance is added to index 1
            hold[1] += line.strip()
    #assign individual sequences a var
    one = hold[0]
    two = hold[1]

#initialize the matrix: q1+1 x q2+1 so the sequence position does not offset indexing
q1 = int(len(one))
q2 = int(len(two))
m = []
for i in range(q1+1):
    m.append([0]*(q2+1))

#put sequence position in matrix
for i in range(q1 + 1):  #first column, begins with int 0, ends in len(q1)
    m[i][0] = i
for j in range(q2 + 1):  #first row, begins with int 0, ends in len(q2)
    m[0][j] = j

#compute the edit distance
#range begins at index 1 so the upper left 0 is not impacted. Int to index = +1
for i in range(1, q1 + 1):
    for j in range(1, q2 + 1):
        if one[i - 1] == two[j - 1]:  # match = 0 penalty
            penalty = 0 
        else:
            penalty = 1  #mismatch/gap = 1 penalty
        #finds the lowest value in squares above, to the left, and diagnal to the target square
        #from Q2 notes at bottom of homework submition
        m[i][j] = min(m[i - 1][j] + 1,  # row above [i][j]
                      m[i][j - 1] + 1,  # column to left of [i][j]
                      m[i - 1][j - 1] + penalty)  #left column and row above target square [i][j](DIAGNAL)
#writes 
with open(outfile, 'w') as output:
    output.write(str(m[q1][q2]))

#python HW2Q1.py --input <> --output <>