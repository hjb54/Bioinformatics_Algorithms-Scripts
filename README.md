# Bioinformatics Algorithms and Scripts
This repo contains small to medium academic assignments from an undergraduate Computational Biology course.
---
## Contents

### 1. Sequence Comparison & Alignment 
#### `levenshtein_distance_fasta.py` 
Computes the Levenshtein edit distance between two FASTA‑formatted sequences using a dynamic programming matrix. 

#### `needleman_wunsch_algorithm.py` 
Performs full global alignment (Needleman–Wunsch) by computing edit distance and backtracking through the DP matrix to reconstruct the optimal alignment with gaps. 

--- 

### 2. FASTQ Quality Control 
#### `fastq_mean_quality_by_position.py` 
Calculates the mean Phred quality score at each base position across all reads and reports how many positions fall below a specified threshold. Implements ASCII‑to‑Phred conversion manually using `ord()`. 

#### `fastq_quality_counter.py` Counts how many FASTQ reads meet user‑defined quality and percentage thresholds using Phred scores extracted via Biopython. 

--- 

### 3. Assembly Metrics 
#### `contig_length_stats.py` 
Computes N50 and N75 values from a list of contig sequences by sorting lengths, calculating cumulative coverage, and identifying the contig length at each threshold. 

---

### 4. Graph‑Based Assembly Algorithms 
#### `debruijn_adjacency_list.py` 
Constructs a de Bruijn graph adjacency list from sequencing reads by generating k‑mer prefix/suffix edges for both reads and their reverse complements. Outputs a sorted adjacency list suitable for downstream graph analysis. 
> **Note:**
> This script includes an unfinished `cycles()` function.
> It is included for documentation of intended logic only and is **not executed**.

---

## Skills Demonstrated 

### Bioinformatics Concepts 
- FASTA and FASTQ parsing
- Phred quality score interpretation
- Read‑level and position‑level QC
- Reverse complements
- k‑mer decomposition
- De Bruijn graph construction
- Assembly metrics (N50, N75)
- Global sequence alignment

### Algorithmic & CS Concepts
- Dynamic programming
- Matrix initialization and backtracking
- Graph representation with adjacency lists
- Sorting and cumulative summation
- ASCII encoding and manual score conversion
- Command‑line interface design with `argparse`
- File I/O and structured output formatting
- Use of Biopython for sequence handling

---

## Usage

Each script follows a consistent command‑line interface pattern: 

```
python script_name.py -i input_file -o output_file
```
Input and output formats vary by script and are described in comments within each file. 

---

## Purpose

This repository serves as a demonstration of foundational computational biology techniques implemented through Python.
