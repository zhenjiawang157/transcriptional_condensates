import os,sys,argparse
# import fileinput,time
import glob
import re,bisect,os
import pandas as pd
import numpy as np
import matplotlib
from scipy import stats



indir = 'f1_bart3d'
outdir = 'f2_DCI_overlap_TFBS_clustered'
os.makedirs(outdir,exist_ok=True)

tfbs_dir = '../../f1_TF_cluster_potential/f2_cor_CP_SE_AICAP/f3_TFBS_CP_heatmap/_csv'   
# tfbs_cp_types = ['CP_TFBS_vs_TFMS',
#                  'CP_TFBS_overlap_motif_vs_TFMS',
#                  'CP_TFBS_NOT_overlap_motif_vs_TFMS']

# atac_file = '../../../f9_TF_condensates_V3/data/TCGA/tcga_atac.bed'
mergefile_dir = '../../f1_TF_cluster_potential/f3_clustered_TFBS/f2_bedfiles_merged/'
# percentile_mergefile_dir = '../../f1_TF_cluster_potential/f3_clustered_TFBS/f2_bedfiles_merge/'

dci_dir = '../../../f11_TF_condensates_KS_test/f3_public_data/f1_hct116_hic_RAD21_auxin/f1_bart3d/'

genomicDistances = [100000, 200000, 500000]
reps = ['rep1','rep2','all_reps']

# for tfbs_cp_type in tfbs_cp_types[:1]:
if 1:
    tfbs_cp_s = pd.read_csv('{}/data_fisher_CP_TFBS_all_vs_TFMS_CP_KStest_statistics.csv'.format(tfbs_dir),index_col=0)
    
#     for ct in ['MCF-7','HCT-116','HeLa','LNCaP','U87','HepG2'][:]:
    for ct in ['HCT-116'][:]:
        factors = tfbs_cp_s[ct].dropna().sort_values(ascending=False).index
        
        for factor in factors[:]:
            for flag in ['percentile_T','percentile_T_ExtendMerge','percentile_C']:
                mergefile = '{}/{}/{}_{}_{}.merge.bed'.format(mergefile_dir,ct,ct,factor,flag)
                                  
                if os.path.isfile(mergefile):     
                    for genomicDis in genomicDistances:  
                        for rep in reps:
                            dci_file = '{}/RAD21_6hr_auxin_over_NT_{}_dis{}k_differential_score.bed'.format(dci_dir,rep,str(int(genomicDis/1000)))       
                            outfile = '{}/DCI_RAD21_KO_{}_dis{}k_overlap_{}_{}_{}.bed'.format(outdir,rep,str(int(genomicDis/1000)),ct,factor,flag)
                            commandLine = 'bedtools intersect -a {} -b {} -wa -c > {}'.format(dci_file,mergefile,outfile)
                            print(commandLine)
                            os.system(commandLine)
    

#         se_file = '../../data/SE_hg38/{}.bed'.format(ct)
#         outfile = '{}/atac_overlap_{}_SE.bed'.format(outdir,ct)
#         commandLine = 'bedtools intersect -a {} -b {} -wa -c > {}\n'.format(atac_file,se_file,outfile)
#         print(commandLine)
#         os.system(commandLine)
# 
# 





