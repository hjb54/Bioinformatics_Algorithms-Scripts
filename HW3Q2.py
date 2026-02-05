import sys
import argparse
from collections import defaultdict

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

# Function to compute the reverse complement
def rev_comp(seq): 
    comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} #comp
    return ''.join(comp[base] for base in reversed(seq)) #reverse

# Function to create the graph adjacency list
def graph(reads):
    adj = defaultdict(set) #each key's valuable is set automatically, no key errors.
    k = len(reads[0])
    for read in reads: #iterate through each read and it's rev comp
        for seq in [read, rev_comp(read)]:
            pre = seq[:-1] #like when doing it by hand, seperating the last bps to find the next node
            suf = seq[1:]
            adj[pre].add(suf) #adding the next set to dict
    return adj

def cycles(adj):
    def visit(node):
        while adj[node]:
            #next node, remove node- maybe pop()
            #visit again
            #appned node for each cycle

# Main function
def start():
    with open(infile, 'r') as file: #opening infile, getting info as lines
        reads = file.read().splitlines()
    reads = list(set(reads)) #converts to set and then back to list, removed duplicates
    adj_list = graph(reads)#returns adj list
    # Write to the output file
    with open(outfile, 'w') as file:
        for pre in sorted(adj_list):  # for each pre-suf pair, its writeen to outfile as "pre suf"
            for suf in sorted(adj_list[pre]):  #forms the adj list of the graph, each edge on a new line
                file.write(f"{pre} {suf}\n")

if __name__ == "__main__":
    start()