#!/bin/bash
#SBATCH --job-name=llama-7b_no_intervention_true
#SBATCH --output=llama-7b_no_intervention_true-concept_v_object_5.out
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --mem=80GB
#SBATCH --time=1:00:00


source /data/jiuding_sun/.bashrc
cd /data/jiuding_sun/function_vectors/src
python evaluation.py --dataset_name concept_v_object_5 --model_name /data/public_models/llama/llama_hf_weights/llama-7b --save_path_root /data/jiuding_sun/function_vectors/results/llama-7b