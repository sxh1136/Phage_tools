#!/usr/bin/env python
### Credit for script goes to Alex Reynolds on bioinformatics stack exchange https://bioinformatics.stackexchange.com/questions/13879/how-to-fragment-genomes-into-non-overlapping-sequences-of-differing-sizes
### For fragmenting genomes uniformly
### ./fragment_genomes <lower bp bound> <higher bp bound> <file_name>
import sys
import numpy as np
import timeit

low = int(sys.argv[1])
high = int(sys.argv[2])
in_fn = sys.argv[3]

"""
Globals
"""
fragment_lengths = []

"""
Process a record
"""
def process_record(header, sequence, low, high):
    next = 0
    last = 0
    fragment = 1
    fragment_sequence = ""
    while last < len(sequence) - high:
        next = np.random.randint(low, high + 1) + last
        fragment_sequence += sequence[last:next]
        sys.stdout.write('{}:{}-{}:{}\n{}\n'.format(header, last, next, fragment, sequence[last:next]))
        #fragment_lengths.append(next - last)                                                                                                                                                                                                                                                                                                                                                                                            
        last = next
        fragment += 1
    """
    Uncomment to compare input sequence with fragments
    """
    #sys.stderr.write('In > {}\nOut > {}\n'.format(sequence, fragment_sequence))
    
"""
Parse records
"""
def parse_records(in_fn, low, high):
    header = ""
    sequence = ""
    with open(in_fn, 'r') as ifh:
        for line in ifh:
            if line.startswith('>'):
                if len(sequence) > 0:
                    process_record(header, sequence, low, high)
                    sequence = ""
                header = line.rstrip()
            else:
                sequence += line.rstrip()
        if len(sequence) > 0:
            process_record(header, sequence, low, high)

def count_elements(seq):
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def main(in_fn, low, high):
    """
    Comment below if testing the distribution of fragments
    """
    parse_records(in_fn, low, high)
    """
    Uncomment to test the distribution of fragments from 
    running fns on same input 100k times
    """
    #wrapped = wrapper(parse_records, in_fn, low, high)
    #timeit.timeit(wrapped, number=100000)
    #print(count_elements(fragment_lengths))

if __name__ == "__main__":
    main(in_fn, low, high)
