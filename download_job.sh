#!/bin/bash
#SBATCH --time=06:00:00
#SBATCH --job-name='download'
#SBATCH --ntasks-per-node=10
#SBATCH --output=%J.out
#-------------------------------------
# Usage:
#    sbatch --export=SRC="<SRC>",DEST="<DEST>" download_job.sh
#-------------------------------------
module load rclone

rclone copy "${SRC}" "${DEST}"
  -P --stats-one-line --transfers 100 # \
  # --drive-shared-with-me
