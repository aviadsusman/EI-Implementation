import os
import pandas as pd
import numpy as np

csvs = "/Users/aviadsusman/PycharmProjects/EI_implement/data"
modalities = {}
for file_name in os.listdir(csvs):
    if not (file_name.startswith('labels') or file_name.startswith('data')):
        file_path = os.path.join(csvs, file_name)
        modality = os.path.splitext(file_name)[0]

        data = pd.read_csv(file_path).to_numpy()
        modalities[modality] = data
y = pd.read_csv('/Users/aviadsusman/PycharmProjects/EI_implement/data/labels.csv', header=None).to_numpy()

for array_name, array in modalities.items():
    print(f"Array '{array_name}' shape: {array.shape}")

print(y.shape)