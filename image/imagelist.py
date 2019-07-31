import os
import pandas as pd

# hardcoded
data_folders = ['cat',
 'car',
 'dog',
 'lion'
 ]
data_folders

# array of arrays, containing the list files, grouped by folder
filenames = [os.listdir(f) for f in data_folders]
[print(f[1]) for f in filenames]
[len(f) for f in filenames]