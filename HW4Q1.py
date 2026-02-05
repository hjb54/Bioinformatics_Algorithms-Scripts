import sys
import argparse
from Bio import SeqIO

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
#^all from class

accepted = 0 #counter for reads that meet expectations

with open(infile, 'r') as file:
    lines = file.readline().strip().split() #space delimeted split
    q_thres = int(lines[0]) #quality threshold, inter value for score (20 in example)
    p_thres = float(lines[1]) #percent threshold, float value for percentage (90 in example)
    
    for ch in SeqIO.parse(file, "fastq"):
        q_score = ch.letter_annotations["phred_quality"] # phred quality scores from character
        bases = [i for i in q_score if i >= q_thres ] # all bases that meet the quality threshold
        p_bases =  (len(bases)/len(q_score)) *100 #caculate percent of acceptable scores of all scores 
        if p_bases >= p_thres: #adds 1 to acceptance counter if the percent threshold is met
            accepted += 1

with open(outfile, 'w') as out:
    out.write(str(accepted))
    
# https://biopython.org/docs/1.75/api/Bio.SeqRecord.html < very helpful in explaining how to use a SeqRecord with the quality scores
