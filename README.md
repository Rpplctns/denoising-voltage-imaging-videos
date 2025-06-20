# Denoising Voltage Imaging Videos
This is a codebase for a research project focused on denoising voltage imaging videos. The project aimed to investigate the suitability of different traditional denoising methods for denoising videos made with this technique.

## Contents
The files in the ```helper_scripts``` directory contain the code used to run the experiments and generate the results presented in the paper. The results are the hyperparametrs tests and the denoised videos. The ```figures``` directory contains the logic to generate graphs and output images.

## Requirements
To run the code, the required python packages must be installed. Moreover, the data required must be put in the data folder. The infrastructure enables to use both data with and without a ground truth.

## Required Python Packages
- numpy
- tifffile
- medpy
- scikit-image
- scipy
- matplotlib
- seaborn
- pandas