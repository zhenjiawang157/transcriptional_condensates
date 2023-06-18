import os,sys,argparse,glob,re
import numpy as np
import pandas as pd
# import find_overlap_keep_info_NOT_sep_strand_asimport




# == main 
outdir1 = 'ATAC_overlap_SE_overlap_TFMS'
outdir2 = 'ATAC_overlap_TFMS'
os.makedirs(outdir1,exist_ok=True)
os.makedirs(outdir2,exist_ok=True)

project_dir='/Volumes/zanglab/zw5j/since2019_projects/phase_separation_FEpiTR/f7_TF_condensates_test'
project_dir='/nv/vol190/zanglab/zw5j/since2019_projects/phase_separation_FEpiTR/f7_TF_condensates_test'
atac_overlap_SE_dir = '{}/f6_revised_TCGA_ATAC_cor_SE/f3_clinical_hicor_SE_overlapped_peaks/f1_clinical_at_each_peak/f1_ATAC_overlap_SE_caseID'.format(project_dir)
atac_file = '{}/f6_revised_TCGA_ATAC_cor_SE/data/TCGA/tcga_atac.bed'.format(project_dir)

motif_file_dir='/nv/vol190/zanglab/shared/Motif/sites/hg38_fimo_jarspar/results/'
motif_infiles = glob.glob('{}/*'.format(motif_file_dir))
motif_infiles = [i for i in motif_infiles if not re.search('~',i)]
motif_infiles.sort()


# read matched names between TCGA ATAC and SE data
name_match = pd.read_excel('TCGA-ATAC_SE_cancerType_match.xlsx',index_col=0)   
name_match = name_match.dropna()
for cancertype in ['BRCA','COAD']:
    cancertype_SE = name_match.loc[cancertype].SE
    cancertype_SE_rename = name_match.loc[cancertype].SE_rename
    atac_overlap_SE_file='{}/{}_ATAC_overlap_{}_SE_caseID.bed'.format(atac_overlap_SE_dir,cancertype,cancertype_SE)
    for motif_file in motif_infiles[:]:
        motif_name = os.path.basename(motif_file).split('.bed')[0]
        output_bed = '{}/{}_ATAC_overlap_{}_SE_overlap_{}.bed'.format(outdir1,cancertype,cancertype_SE,motif_name)
        commandLine = 'bedtools intersect -a {} -b {} -wa -u > {}\n'.format(atac_overlap_SE_file,motif_file,output_bed)
        os.system(commandLine);print(commandLine)
            

for motif_file in motif_infiles[:]:
    motif_name = os.path.basename(motif_file).split('.bed')[0]
    output_bed = '{}/ATAC_overlap_{}.bed'.format(outdir2,motif_name)
    commandLine = 'bedtools intersect -a {} -b {} -wa -u > {}\n'.format(atac_file,motif_file,output_bed)
    os.system(commandLine);print(commandLine)
            

  

