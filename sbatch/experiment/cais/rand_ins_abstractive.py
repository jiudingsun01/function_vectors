import os
import json


if __name__ == "__main__":
    
    model_path = "/data/public_models/llama/llama_hf_weights/llama-7b"
    flan_model_path = "/data/jiuding_sun/function_vectors/flan-llama-7b"
    
    flan_cie_save_path = "/data/jiuding_sun/function_vectors/results/INS/CIE-Rand/flan-llama-7b"
    
    llama_fv_save_path = "/data/jiuding_sun/function_vectors/results/INS/FV-Rand/llama-7b_with_flan_fv"
    flan_fv_save_path = "/data/jiuding_sun/function_vectors/results/INS/FV-Rand/flan-llama-7b"
    
    experiment_name = "rand-ins-abstractive"
    
    all_datasets = ["antonym", "capitalize_second_letter", "country-currency", "present-past", "sentiment"]
    print(all_datasets)
    
    all_sbatch_files = []
    
    if not os.path.exists(f"../../scripts/{experiment_name}"):
        os.makedirs(f"../../scripts/{experiment_name}")
        
    for dataset_name in all_datasets:
                
        flan_mean_activations_path = os.path.join(flan_cie_save_path, dataset_name, f"{dataset_name}_mean_head_activations.pt")
        flan_indirect_effect_path = os.path.join(flan_cie_save_path, dataset_name, f"{dataset_name}_indirect_effect.pt")
        
        prompt_1_cie_save_path = os.path.join(flan_cie_save_path, f"Prompt1")
        prompt_1_flan_mean_activations_path = os.path.join(prompt_1_cie_save_path, dataset_name, f"{dataset_name}_mean_head_activations.pt")
        prompt_1_flan_indirect_effect_path = os.path.join(prompt_1_cie_save_path, dataset_name, f"{dataset_name}_indirect_effect.pt")
        prompt_1_llama_fv_save_path = os.path.join(llama_fv_save_path, f"Prompt1")
        prompt_1_flan_fv_save_path = os.path.join(flan_fv_save_path, f"Prompt1")
        
        prompt_2_cie_save_path = os.path.join(flan_cie_save_path, f"Prompt2")
        prompt_2_flan_mean_activations_path = os.path.join(prompt_2_cie_save_path, dataset_name, f"{dataset_name}_mean_head_activations.pt")
        prompt_2_flan_indirect_effect_path = os.path.join(prompt_2_cie_save_path, dataset_name, f"{dataset_name}_indirect_effect.pt")
        prompt_2_llama_fv_save_path = os.path.join(llama_fv_save_path, f"Prompt2")
        prompt_2_flan_fv_save_path = os.path.join(flan_fv_save_path, f"Prompt2")
        
        prompt_3_cie_save_path = os.path.join(flan_cie_save_path, f"Prompt3")
        prompt_3_flan_mean_activations_path = os.path.join(prompt_3_cie_save_path, dataset_name, f"{dataset_name}_mean_head_activations.pt")
        prompt_3_flan_indirect_effect_path = os.path.join(prompt_3_cie_save_path, dataset_name, f"{dataset_name}_indirect_effect.pt")
        prompt_3_llama_fv_save_path = os.path.join(llama_fv_save_path, f"Prompt3")
        prompt_3_flan_fv_save_path = os.path.join(flan_fv_save_path, f"Prompt3")
        
        prompt_4_cie_save_path = os.path.join(flan_cie_save_path, f"Prompt4")
        prompt_4_flan_mean_activations_path = os.path.join(prompt_4_cie_save_path, dataset_name, f"{dataset_name}_mean_head_activations.pt")
        prompt_4_flan_indirect_effect_path = os.path.join(prompt_4_cie_save_path, dataset_name, f"{dataset_name}_indirect_effect.pt")
        prompt_4_llama_fv_save_path = os.path.join(llama_fv_save_path, f"Prompt4")
        prompt_4_flan_fv_save_path = os.path.join(flan_fv_save_path, f"Prompt4")
        
        prompt_5_cie_save_path = os.path.join(flan_cie_save_path, f"Prompt5")
        prompt_5_flan_mean_activations_path = os.path.join(prompt_5_cie_save_path, dataset_name, f"{dataset_name}_mean_head_activations.pt")
        prompt_5_flan_indirect_effect_path = os.path.join(prompt_5_cie_save_path, dataset_name, f"{dataset_name}_indirect_effect.pt")
        prompt_5_llama_fv_save_path = os.path.join(llama_fv_save_path, f"Prompt5")
        prompt_5_flan_fv_save_path = os.path.join(flan_fv_save_path, f"Prompt5")
        
        with open(f"../../scripts/{experiment_name}/{dataset_name}.sh", 'w') as f:
            f.write("#!/bin/bash\n")
            f.write(f"#SBATCH --job-name={experiment_name}\n")
            f.write(f"#SBATCH --output={experiment_name}-{dataset_name}.out\n")
            f.write("#SBATCH --nodes=1\n")
            f.write("#SBATCH --gpus-per-node=1\n")
            f.write("#SBATCH --mem=32GB\n")
            f.write("#SBATCH --time=12:00:00\n")
            
            f.write("\n\n")
            f.write("source /data/jiuding_sun/miniconda3/bin/activate\n")
            f.write("cd /data/jiuding_sun/function_vectors/src\n")
            f.write("conda activate fv\n")
            f.write("\n\n")
            f.write(f"python compute_indirect_effect.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_1_cie_save_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--instruction_ablation random ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/1/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/1/separators.json ")
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_1_flan_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_1_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_1_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/1/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/1/separators.json ")     
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {model_path} ")
            f.write(f"--save_path_root {prompt_1_llama_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_1_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_1_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/1/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/1/separators.json ")     
            f.write(f"&&\n")
            
            f.write(f"python compute_indirect_effect.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_2_cie_save_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--instruction_ablation random ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/2/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/2/separators.json ")
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_2_flan_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_2_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_2_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/2/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/2/separators.json ")     
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {model_path} ")
            f.write(f"--save_path_root {prompt_2_llama_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_2_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_2_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/2/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/2/separators.json ")     
            f.write(f"&&\n")
            
            f.write(f"python compute_indirect_effect.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_3_cie_save_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--instruction_ablation random ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/3/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/3/separators.json ")
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_3_flan_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_3_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_3_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/3/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/3/separators.json ")     
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {model_path} ")
            f.write(f"--save_path_root {prompt_3_llama_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_3_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_3_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/3/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/3/separators.json ")     
            f.write(f"&&\n")
            
            f.write(f"python compute_indirect_effect.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_4_cie_save_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--instruction_ablation random ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/4/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/4/separators.json ")
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_4_flan_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_4_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_4_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/4/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/4/separators.json ")     
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {model_path} ")
            f.write(f"--save_path_root {prompt_4_llama_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_4_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_4_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/4/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/4/separators.json ")     
            f.write(f"&&\n")
            
            f.write(f"python compute_indirect_effect.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_5_cie_save_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--instruction_ablation random ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/5/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/5/separators.json ")
            f.write(f"&&\n")
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {flan_model_path} ")
            f.write(f"--save_path_root {prompt_5_flan_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_5_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_5_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/5/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/5/separators.json ") 
            f.write(f"&&\n") 
            f.write(f"python evaluate_function_vector.py ")
            f.write(f"--dataset_name {dataset_name} ")
            f.write(f"--model_name {model_path} ")
            f.write(f"--save_path_root {prompt_5_llama_fv_save_path} ")
            f.write(f"--mean_activations_path {prompt_5_flan_mean_activations_path} ")
            f.write(f"--indirect_effect_path {prompt_5_flan_indirect_effect_path} ")
            f.write(f"--n_shots 0 ")
            f.write(f"--n_trials 100 ")
            f.write(f"--prefixes /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/5/prefixes.json ")
            f.write(f"--separators /data/jiuding_sun/function_vectors/templates_files/abstractive/{dataset_name}/5/separators.json ")     
            f.close()
            
        all_sbatch_files.append(f"../../scripts/{experiment_name}/{dataset_name}.sh")
        
    for f in all_sbatch_files:
        os.system(f"sbatch {f}")
            