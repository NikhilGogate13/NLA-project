import numpy as np
from numpy import linalg as LA
from sklearn.preprocessing import normalize
import argparse
import os.path

maxs = 200
parser = argparse.ArgumentParser(description='document parser')
parser.add_argument("--source", type=str, help="source embedding file")
parser.add_argument("--target", type=str, help="target embedding file")
parser.add_argument("--output", type=str, help="output file")

params = parser.parse_args()
my_path = os.path.abspath(os.path.dirname(__file__))
params.source = os.path.join(my_path, params.source)
params.target = os.path.join(my_path, params.target)
params.output = os.path.join(my_path, params.output)
source = np.load(params.source)[:maxs, :]
target = np.load(params.target)[:maxs, :]


source_marker = np.zeros(np.shape(source)[0])
# for cosine similarity
source = normalize(source)
target = normalize(target)
score = np.matmul(source, np.transpose(target))

mapping = []

for i in range(target.shape[0]):
    maxim = -np.inf
    index = 0
    for j in range(source.shape[0]):
        if source_marker[j] == 1:
            continue
        # if maxim < score[j, i]:
        if maxim < score[j, i]:
            maxim = score[j, i]
            index = j
    source_marker[index] = 1
    mapping.append((i, index))

print(mapping)
