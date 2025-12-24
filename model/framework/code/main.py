# imports
import os
import sys
import numpy as np
from eosce.models import ErsiliaCompoundEmbeddings
from ersilia_pack_utils.core import read_smiles, write_out

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles_list):
    model = ErsiliaCompoundEmbeddings()
    embeddings = model.transform(smiles_list)
    print(embeddings)
    return embeddings

# read input
_, smiles_list = read_smiles(input_file)

# run model
outputs = my_model(smiles_list)

input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

header = ["dim_{:04d}".format(i) for i in range(1024)]

# write output in a .csv file
write_out(outputs, header, output_file, np.float32)
