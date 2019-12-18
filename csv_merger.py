import glob
import os
import sys

import pandas as pd

execution_path = os.path.dirname(sys.executable)

if sys.platform == 'darwin':
    os.chdir(execution_path)

all_files = glob.glob(execution_path+"/*.csv")

li = []

for index, filename in enumerate(all_files):
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    print('{}%'.format(int(100*(index+1)/len(all_files))), end='\r')


frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv('merge_result.csv', index=False)
