#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --job-name='detect'
#SBATCH --ntasks-per-node=50
#SBATCH --error=%J.err
#SBATCH --output=%J.out
#-------------------------------------
# Usage:
#    sbatch --export=DIR_PATH="<DIR_PATH>" detect_job.sh
#-------------------------------------
module load anaconda
conda activate yolov5

python prepare.py "${DIR_PATH}"
