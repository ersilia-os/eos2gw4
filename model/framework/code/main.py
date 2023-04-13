# imports
import os
import csv
import sys
from eosce.models import ErsiliaCompoundEmbeddings

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


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["feature{}".format(i) for i in range(1024)])  # header
    for o in outputs:
        writer.writerow(o)
