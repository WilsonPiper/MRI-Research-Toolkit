'''
activate virtual environment: source venv/bin/activate

Open Docker:
docker run -it --rm \
  --entrypoint bash \
  -m 10g \
  --memory-swap 10g \
  -v "/Users/lxl/freesurfer-freesurfer-dev-mri_WMHsynthseg/WMHSynthSeg:/code" \
  -v "/Users/lxl/Desktop/Summer_Research/SynthSeg/flair:/data" \
  pablaso/wmh_synthseg

python3 /code/inference.py \
  --i /data/I1005742_Sagittal_3D_FLAIR_20180604135315_3_Downscaled.nii.gz \
  --o /data/I1005742_Sagittal_3D_FLAIR_20180604135315_3_Downscaled_Output.nii.gz \
  --device cpu \
  --threads 1

Second usage way:
export FREESURFER_HOME=/Applications/freesurfer/8.0.0
source $FREESURFER_HOME/SetUpFreeSurfer.sh


'''

import nibabel as nib
import numpy as np
from nilearn.image import resample_img

# Load the original image
img = nib.load("/Users/lxl/Desktop/Summer_Research/SynthSeg/flair/I1005742_Sagittal_3D_FLAIR_20180604135315_3.nii.gz")

# Get the voxel array
data = img.get_fdata()

# Get shape and voxel count
voxel_shape = data.shape
total_voxels = np.prod(voxel_shape)

print(f"Voxel shape: {voxel_shape}")
print(f"Total voxels: {total_voxels}")

# Set target voxel size (e.g. 2mm isotropic instead of 1mm)
target_affine = np.diag([4, 4, 4])  # X, Y, Z spacing

# Resample image
resampled = resample_img(img, target_affine=target_affine)

# Save the downsampled image
resampled.to_filename("/Users/lxl/Desktop/Summer_Research/SynthSeg/flair/I1005742_Sagittal_3D_FLAIR_20180604135315_3_Downscaled.nii.gz")

# Get the voxel array
resampled_data = resampled.get_fdata()

# Get shape and voxel count
voxel_shape = resampled_data.shape
total_voxels = np.prod(voxel_shape)

print(f"New Voxel shape: {voxel_shape}")
print(f"New Total voxels: {total_voxels}")