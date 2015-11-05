__author__ = 'rain'

from solution import *

import pandas as pd

collatz_graph = pd.DataFrame({
    "source": [],
    "target": []
})

N = int(5e2)

print "Generate Collatz Graph Program"
print "Number of nodes: {}".format(N)

print "\nStart Generate Collatz Sequences"
for i in range(1, N):
    if i % 100000 == 0:
        print i
    generate_sequence(i)
print "Finish Generate Collatz Sequences"

print "Start Generate Collatz Graph"
for sequence in sequences.values():
    if sequence != [1]:
        for i in range(len(sequence) - 1):
            source = sequence[i]
            target = sequence[i+1]
            if source in collatz_graph["source"].values:
                break
            else:
                edge = [{"source": sequence[i], "target": sequence[i+1]}]
                collatz_graph = collatz_graph.append(edge)
collatz_graph = collatz_graph.drop_duplicates()
collatz_graph = collatz_graph.astype(int)
print "Finish Generate Collatz Graph"

filename = "collatz_graph_{}_node.csv".format(N)
print "Start Write Collatz Graph to File : {}".format(filename)
collatz_graph.to_csv(filename, header=False, index=False)
print "Finish Write Collatz Graph to File {}".format(filename)

