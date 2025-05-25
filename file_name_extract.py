import os

#change the following file path 
path = "/Users/lxl/Desktop/Summer Research/NeuroT-Map-main/lesions"
files = os.listdir(path)
resultant_files = []

for f in files:
    length = len(f)
    if (f[length-4:length:1] == ".nii") or (f[length-7:length:1] == ".nii.gz"):
        resultant_files.append(f)

for names in resultant_files:
    print(f"{names} ", end= '')