import sys
import argparse
from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator # came across when finding letter_annotations

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

#pretty much the same as before, but this time considering x reads of y base- trying a different method using FASTqGnerealIterator

q_pos = [] # initalizing list that will have a index for each base
reads = 0 #counter for reads in file

with open(infile, 'r') as file:
    q_thres = int(file.readline().strip()) # takes quality score, integer value
    
    for read, seq, q in FastqGeneralIterator(file): #iterates over fastq as string tuples of title, sequence and quality. removes whitespace too
        q_score = [ord(i) - 33 for i in q] #coverting ASCI to PHRED ord('!') - 33 = 0 https://biopython.org/docs/latest/api/Bio.SeqIO.QualityIO.html
        
        if reads == 0:
            q_pos = [0] * len(q_score) #adding in the indexes for each base
        
        for x, score in enumerate(q_score):
            q_pos[x] += score #adds up all the scores for each base in it's index

        reads += 1 #increase counter to next read
    
    mean_q = [z / reads for z in q_pos] #divids sum by # of reads for each index
    unacceptable = sum(1 for q in mean_q if q < q_thres) # adds 1 if the mean quality score is subpar for q base

with open(outfile, 'w') as out:
    out.write(str(unacceptable))