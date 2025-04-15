# Deeplearning-MLOps

## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the componets
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

## How to run ?
### Steps:

Clone the repository
```bash
git clone https://github.com/naseemap47/Deeplearning-MLOps
```
### Step 01 - Create conda env
```bash
cd Deeplearning-MLOps/
conda create -n mlops python=3.10 -y
```

### Step 01 - Install the requirements
```bash
conda activate mlops
sudo apt install libpq-dev python3-dev
pip install -r requirements.txt
```

