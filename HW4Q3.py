import sys
import argparse

# Function to parse command line arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description="Generate the adjacency list of a de Bruijn graph from sequencing reads.")
    parser.add_argument("-i", "--input", help="input file", required=True)
    parser.add_argument("-o", "--output", help="output file", required=True)
    return parser.parse_args(args)

# Retrieve command line arguments
arguments = check_arg(sys.argv[1:])
infile = arguments.input
outfile = arguments.output
# ^all from class

with open(infile, 'r') as file:
    contigs = [line.strip() for line in file] #iterates for all lines in file, strips

tot = sum(len(contig) for contig in contigs) #finds sum of lengths using each value in contigs list 
sort = sorted(contigs, key = len, reverse = True) #sorting contigs by length, in descending order

#initalizing variables for sum of lengths
sum50 = 0 
sum75 = 0

#initalizing the thresholds for N50 and N75
thres50 = 0.5 * tot
thres75 = 0.75 * tot

#initalizing empty vars for the N50 N75 values
n50 = 0
n75 = 0

for contig in sort: #calculate n50
    sum50 += len(contig)
    if sum50 >= thres50:
        n50 = len(contig)
        break #stop once found

for contig in sort: #calculate n75
    sum75 += len(contig)
    if sum75 >= thres75:
        n75 = len(contig)
        break #stop once found

with open(outfile, 'w') as out: #write to outfile
    out.write(str(n50) + ' ' + str(n75))