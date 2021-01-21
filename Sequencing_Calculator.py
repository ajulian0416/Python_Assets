import sys,argparse

usage = """
Version 0.0.1
Date 1/20/21
Author A. Julian

This is a tool used to determine how many cells were in a culture based on the mass of a DNA pellet,
or how many cells are required to obtain a specific amount of DNA for sequencing.

-n | --count\t The number of cells present in the culture
-c | --content\t [optional] The GC content of the genome (decimal)
-l | --length\t The length of the the organisms genome
-w | --ploidy\t The number of copies of chromosomes (default: 1, haploid)
-p | --pellet\t The mass of the DNA pellet [micrograms]
-m | --mass\t The desired amount of mass [micrograms]
-s | --sequencer\t [optional] The sequencer that is to be used {nanopore, illumina, pacbio}

Examples

Sequencing_Calculator.py -n 10*4 -l 2.5*10**6 -c .46

Sequencing_Calculator.py -l 2.5*10**6 -s nanopore

Sequencing_Calculator.py -l 2.5*10**6 -m 1.5
"""

if len(sys.argv) == 1:
    print(usage)

parser = argparse.ArgumentParser()
parser.add_argument("-n","--count",type=float)
parser.add_argument("-c","--content",type=float)
parser.add_argument("-l","--length",type=float)
parser.add_argument("-p","--ploidy",type=int)
parser.add_argument("-w","--pellet",type=float)
parser.add_argument("-m","--mass",type=float)
parser.add_argument("-s","--sequencer",type=float)

args = parser.parse_args()

if not args.length:
    print("The estimated genome legnth is required for calculations...")
    sys.exit()
if not args.mass or not args.pellet:
    print("Calculating the mass yeild from cell count...")
elif not args.count:
    print("Calculating the number of cells required for sequencing...")
else:
    print("Either the number of cells or the mass obtained/required is needed for calculations...")