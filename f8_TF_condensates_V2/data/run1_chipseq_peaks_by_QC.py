import sys,argparseimport os,globimport numpy as npimport pandas as pdimport re,bisect# ==== keep high quality data# data_dir = '/nv/vol190/zanglab/zw5j/data/cistrome/cistrome_db_2019_new'data_dir = '/Volumes/zanglab/zw5j/data/cistrome/cistrome_db_2019_new'df = pd.read_csv('{}/human_factor_full_QC.txt'.format(data_dir),sep='\t',index_col=0)df = df[(df.PeaksFoldChangeAbove10>200)&(df.FastQC>10)&        (df.UniquelyMappedRatio>0.1)&(df.FRiP>0.001)]dddf.to_csv('cistrome2019_selected_QC.csv')           # ==== count the data per cell type per factorcelltypes = sorted(df.Cell_line.unique())factors = sorted(df.Factor.unique())df_out = pd.DataFrame(index=factors, columns=celltypes).fillna(0)for ii in df.index:    factor = df.loc[ii,'Factor']    celltype = df.loc[ii,'Cell_line']    df_out.loc[factor,celltype]+=1# == repeatively remove sparse elementsnum_thre = 1df_out = df_out.loc[df_out.astype(bool).sum(axis=1)>=num_thre,                    df_out.astype(bool).sum(axis=0)>=num_thre]# == sort columns by total number of datadf_out = df_out.loc[df_out.astype(bool).sum(axis=1).sort_values(ascending=False).index]df_out = df_out[df_out.astype(bool).sum().sort_values(ascending=False).index]df_out.to_csv('cistrome2019_data_Count.csv')        # ==== check overlap with motif and SE# motif_dir="/nv/vol190/zanglab/shared/Motif/sites/hg38_fimo_jarspar/results/"motif_dir="/Volumes/zanglab/shared/Motif/sites/hg38_fimo_jarspar/results/"motif_files = glob.glob('{}/*.bed'.format(motif_dir))motifs = [os.path.basename(i).split("_")[0] for i in motif_files if not re.search('~',i)]SE_files = glob.glob('SE_hg38/*.bed')SEs = [os.path.basename(i).split(".bed")[0] for i in SE_files ]df_out = df_out.loc[df_out.index.intersection(motifs),                    df_out.columns.intersection(SEs)]df_out = df_out.loc[df_out.astype(bool).sum(axis=1)>=num_thre,                    df_out.astype(bool).sum(axis=0)>=num_thre]df_out.to_csv('cistrome2019_data_Count_with_SE_motif.csv')