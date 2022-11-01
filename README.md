# MegaDetector-SLURM


## Setup

- Clone the repository

```sh
git clone https://github.com/Alyetama/MegaDetector-SLURM.git
cd MegaDetector-SLURM
git clone https://github.com/ultralytics/yolov5.git
```

- Download MegaDetector v5 weights

```sh
curl -L https://github.com/microsoft/CameraTraps/releases/download/v5.0/md_v5a.0.0.pt \
  --output 'md_v5a.0.0.pt'
```

- Create a conda environment

```sh
module load anaconda || module load conda
conda create -n yolov5 python=3.8 --yes
conda activate yolov5
pip install -r yolov5/requirements.txt
```
