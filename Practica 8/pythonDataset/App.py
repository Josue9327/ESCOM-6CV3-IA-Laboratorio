import os

file_path = os.path.join(os.path.dirname(__file__), 'bezdekIris.data')
data_matrix = []
with open(file_path, 'r') as file:
    for line in file:
        row = line.strip().split() 
        data_matrix.append(row)
for row in data_matrix:
    print(row)
