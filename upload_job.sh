#!/bin/bash
#SBATCH --time=04:00:00
#SBATCH --job-name='upload'
#SBATCH --ntasks-per-node=10
#SBATCH --output=%J.out
#-------------------------------------
# Usage:
#    sbatch --export=SRC="<SRC>",DEST="<DEST>" upload_job.sh
#-------------------------------------
module load rclone

rclone sync "${SRC}" "${DEST}" \
    -P --stats-one-line --transfers 100
