# requirements
3H8K_complete_seq_noHOH.pdb #the PDB file prepared for the calculation
mutation_list.txt           #list of all amino acids to mutate with
repair_runfile_template.txt
mutate_runfile_template.txt

# activate conda environment
conda activate /home/ctools/protein_structure_course

# run NACCESS for estimating solvent accessibility of the protein residues
naccess 3H8K_complete_seq_noHOH.pdb

# prepare poslist.txt with the residue of interest (residue, chain, residue number)
syntax: 
        EA31
        EA38
        EA45
        LA163
        SA122
        VA138
        WA37
        FA34
        PA20
        RA145

# run mutatex 
nohup mutatex 3H8K_complete_seq_noHOH.pdb -p 1 -m mutation_list.txt -x /home/ctools/foldx/foldx -f suite5 -R repair_runfile_template.txt -M  mutate_runfile_template.txt -q poslist.txt -L -l -v -C deep -c &

#run ddg2excel to get the final csv file with the results
ddg2excel -p 3H8K_complete_seq_noHOH.pdb -l mutation_list.txt -q poslist.txt -d results/mutation_ddgs/3H8K_complete_seq_noHOH_model0_checked_Repair/ -F csv
