import os

#TODO: change the following file path name
path = "/Users/lxl/Desktop/Summer Research/NeuroT-Map-main/lesions"
files = os.listdir(path)

for f in files:
    length = len(f)
    if (f[length-4:length:1] == ".nii"):
        print(f"{f[:length-4]}", end= ' ')
    elif (f[length-7:length:1] == ".nii.gz"):
        print(f"{f[:length-7]}", end = ' ')
