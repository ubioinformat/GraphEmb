import numpy as np
import pandas as pd
import random
import os
#!pip install PyTDC
from tdc.multi_pred import DTI


data = DTI(name = 'BindingDB_Kd')
data.harmonize_affinities(mode = 'max_affinity')
#data.harmonize_affinities(mode = 'mean')

df = data.get_data()
df = df.rename(columns ={'Drug':'SMILES', 'Target':'Target Sequence'})

drugs = df['SMILES'].unique()
genes = df['Target Sequence'].unique()

threshold = 30

df['Label'] = [1 if x < threshold else 0 for x in df['Y']]

print(len(drugs))
print(len(genes))

print(df['Label'].value_counts())

#Save it as a csv files
output_path = os.getcwd() + '/../Data/BindingDB.csv'
df.to_csv('BINDINGDB.csv')