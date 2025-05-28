#external package requirement: nibabel, numpy, and nilearn
import nibabel as nib
import numpy as np
from nilearn import plotting


img = nib.load('path')

data = img.get_fdata()

#the following part is optional based on the need of individuals
print("data shape:", data.shape)
print("data type:", data.dtype)
print("Affine matrix:\n", img.affine)
print("Header info:\n", img.header)

# plot the graph
plotting.view_img(img).open_in_browser()